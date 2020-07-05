"""
<plugin key="Zigbee2MQTT" name="Zigbee2MQTT" version="0.2.0">
    <description>
      Plugin to add support for <a href="https://github.com/Koenkk/zigbee2mqtt">zigbee2mqtt</a> project<br/><br/>
      Specify MQTT server and port.<br/>
      <br/>
      Automatically creates Domoticz devices for connected device.<br/>
    </description>
    <params>
        <param field="Address" label="MQTT Server address" width="300px" required="true" default="127.0.0.1"/>
        <param field="Port" label="Port" width="300px" required="true" default="1883"/>
        <param field="Username" label="MQTT Username (optional)" width="300px" required="false" default=""/>
        <param field="Password" label="MQTT Password (optional)" width="300px" required="false" default="" password="true"/>
        <param field="Mode3" label="MQTT Client ID (optional)" width="300px" required="false" default=""/>
        <param field="Mode1" label="Zigbee2Mqtt Topic" width="300px" required="true" default="zigbee2mqtt"/>
        <param field="Mode6" label="Debug" width="75px">
            <options>
                <option label="Verbose" value="Verbose"/>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal" default="true" />
            </options>
        </param>
    </params>
</plugin>
"""
import Domoticz
import json
import time
import re
import os
from shutil import copy2, rmtree
from mqtt import MqttClient
from api import API
from devices_manager import DevicesManager
from groups_manager import GroupsManager

class BasePlugin:
    mqttClient = None

    def onStart(self):
        self.debugging = Parameters["Mode6"]
        
        if self.debugging == "Verbose":
            Domoticz.Debugging(2+4+8+16+64)
        if self.debugging == "Debug":
            Domoticz.Debugging(2)

        Domoticz.Debug("onStart called")
        self.install()
        self.base_topic = Parameters["Mode1"].strip()
        self.subscribed_for_devices = False

        mqtt_server_address = Parameters["Address"].strip()
        mqtt_server_port = Parameters["Port"].strip()
        mqtt_client_id = Parameters["Mode3"].strip()
        self.mqttClient = MqttClient(mqtt_server_address, mqtt_server_port, mqtt_client_id, self.onMQTTConnected, self.onMQTTDisconnected, self.onMQTTPublish, self.onMQTTSubscribed)

        self.api = API(Devices, self.onApiCommand)
        self.devices_manager = DevicesManager()
        self.groups_manager = GroupsManager()

    def checkDevices(self):
        Domoticz.Debug("checkDevices called")

    def onStop(self):
        Domoticz.Debug("onStop called")
        self.uninstall()


    def onCommand(self, Unit, Command, Level, Color):
        Domoticz.Debug("onCommand: " + Command + ", level (" + str(Level) + ") Color:" + Color)

        message = None
        device = Devices[Unit] #Devices is Domoticz collection of devices for this hardware
        device_params = device.DeviceID.split('_')
        entity_id = device_params[0]

        if (self.devices_manager.get_device_by_id(entity_id) != None):
            message = self.devices_manager.handle_command(Devices, device, Command, Level, Color)
        elif(self.groups_manager.get_group_by_deviceid(device.DeviceID) != None):
            message = self.groups_manager.handle_command(device, Command, Level, Color)
        else:
            Domoticz.Log('Can\'t process command from device "' + device.Name + '"')

        if (message != None):
            self.publishToMqtt(message['topic'], message['payload'])

    def onApiCommand(self, command, data):
        if command == 'publish_mqtt':
            return self.publishToMqtt(data['topic'], data['payload'])
        elif command == 'remove_device':
            return self.devices_manager.remove(Devices, data)
        else:
            Domoticz.Error('Internal API command "' + command +'" is not supported by plugin')

    def publishToMqtt(self, topic, payload):
        self.mqttClient.publish(self.base_topic + '/' + topic, payload)

    def onConnect(self, Connection, Status, Description):
        Domoticz.Debug("onConnect called")
        self.mqttClient.onConnect(Connection, Status, Description)

    def onDisconnect(self, Connection):
        self.mqttClient.onDisconnect(Connection)

    def onDeviceModified(self, unit):
        if (unit == 255):
            self.api.handle_request(Devices[unit].sValue)
            return

    def onMessage(self, Connection, Data):
        self.mqttClient.onMessage(Connection, Data)

    def onHeartbeat(self):
        self.mqttClient.onHeartbeat()

    def onMQTTConnected(self):
        self.mqttClient.subscribe([self.base_topic + '/bridge/#'])

    def onMQTTDisconnected(self):
        self.subscribed_for_devices = False

    def onMQTTSubscribed(self):
        Domoticz.Debug("onMQTTSubscribed")

    def onMQTTPublish(self, topic, message):
        Domoticz.Debug("MQTT message: " + topic + " " + str(message))
        topic = topic.replace(self.base_topic + '/', '')

        self.api.handle_mqtt_message(topic, message)

        if (topic == 'bridge/config/permit_join' or topic == 'bridge/config/devices'):
            return

        if (topic == 'bridge/config'):
            permit_join = 'enabled' if message['permit_join'] else 'disabled'
            Domoticz.Debug('Zigbee2mqtt log level is ' + message['log_level'])
            Domoticz.Log('Joining new devices is ' + permit_join + ' on the zigbee bridge')
            return

        if (topic == 'bridge/state'):
            Domoticz.Log('Zigbee2mqtt bridge is ' + message)

            if message == 'online':
                self.publishToMqtt('bridge/config/devices', '')
                self.publishToMqtt('bridge/config/groups', '')

            return

        if (topic == 'bridge/log'):
            is_connected = message['type'] == 'device_connected'
            is_removed = message['type'] == 'device_removed'
            is_paired = message['type'] == 'pairing' and message['message'] == 'interview_successful'

            if message['type'] == 'devices':
                Domoticz.Log('Received available devices list from bridge')
                
                self.devices_manager.clear()
                self.devices_manager.update(Devices, message['message'])
                
                if self.subscribed_for_devices == False:
                    self.mqttClient.subscribe([self.base_topic + '/+'])
                    self.subscribed_for_devices = True

            if message['type'] == 'groups':
                Domoticz.Log('Received groups list from bridge')
                self.groups_manager.register_groups(Devices, message['message'])

            if is_connected or is_removed or is_paired:
                self.publishToMqtt('bridge/config/devices', '')

            if message['type'] == 'ota_update':
                Domoticz.Log(message['message'])

            if message['type'] == 'zigbee_publish_error':
                #an error occured on publish to the zigbee network
                deviceMeta = message['meta']
                Domoticz.Error("A Zigbee publish error occured for device '" + deviceMeta['friendly_name'] + "' with error message: " + message['message'])

            return

        if (self.devices_manager.get_device_by_name(topic) != None):
            self.devices_manager.handle_mqtt_message(Devices, topic, message)
        elif (self.groups_manager.get_group_by_name(topic) != None):
            self.groups_manager.handle_mqtt_message(topic, message)

    def install(self):
        Domoticz.Log('Installing plugin custom page...')

        try:
            source_path = os.path.dirname(os.path.abspath(__file__)) + '/frontend'
            templates_path = os.path.abspath(source_path + '/../../../www/templates')
            dst_plugin_path = templates_path + '/zigbee2mqtt'

            Domoticz.Debug('Copying files from ' + source_path + ' to ' + templates_path)

            if not (os.path.isdir(dst_plugin_path)):
                os.makedirs(dst_plugin_path)

            copy2(source_path + '/zigbee2mqtt.html', templates_path)
            copy2(source_path + '/zigbee2mqtt.js', templates_path)
            copy2(source_path + '/zigbee_devices.js', dst_plugin_path)
            copy2(source_path + '/zigbee_groups.js', dst_plugin_path)
            copy2(source_path + '/libs/leaflet.js', dst_plugin_path)
            copy2(source_path + '/libs/leaflet.css', dst_plugin_path)
            copy2(source_path + '/libs/viz.js', dst_plugin_path)
            copy2(source_path + '/libs/viz.full.render.js', dst_plugin_path)
            
            Domoticz.Log('Installing plugin custom page completed.')
        except Exception as e:
            Domoticz.Error('Error during installing plugin custom page')
            Domoticz.Error(repr(e))

    def uninstall(self):
        Domoticz.Log('Uninstalling plugin custom page...')

        try:
            templates_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../../www/templates')
            dst_plugin_path = templates_path + '/zigbee2mqtt'

            Domoticz.Debug('Removing files from ' + templates_path)

            if (os.path.isdir(dst_plugin_path)):
                rmtree(dst_plugin_path)

            if os.path.exists(templates_path + "/zigbee2mqtt.html"):
                os.remove(templates_path + "/zigbee2mqtt.html")

            if os.path.exists(templates_path + "/zigbee2mqtt.js"):
                os.remove(templates_path + "/zigbee2mqtt.js")

            Domoticz.Log('Uninstalling plugin custom page completed.')
        except Exception as e:
            Domoticz.Error('Error during uninstalling plugin custom page')
            Domoticz.Error(repr(e))


global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()
    
def onConnect(Connection, Status, Description):
    global _plugin
    _plugin.onConnect(Connection, Status, Description)

def onDeviceModified(Unit):
    global _plugin
    _plugin.onDeviceModified(Unit)

def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)

def onMessage(Connection, Data):
    global _plugin
    _plugin.onMessage(Connection, Data)

def onCommand(Unit, Command, Level, Color):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Color)

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()
