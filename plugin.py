"""
<plugin key="Zigbee2MQTT" name="Zigbee2MQTT" version="0.0.20">
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
        <param field="Mode2" label="Zigbee pairing" width="75px" required="true">
            <options>
                <option label="Enabled" value="true"/>
                <option label="Disabled" value="false" default="true" />
            </options>
        </param>
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
from mqtt import MqttClient
from zigbee_message import ZigbeeMessage
from device_storage import DeviceStorage
from adapters import adapter_by_model

class BasePlugin:
    mqttClient = None

    def onStart(self):
        self.debugging = Parameters["Mode6"]
        
        if self.debugging == "Verbose":
            Domoticz.Debugging(2+4+8+16+64)
        if self.debugging == "Debug":
            Domoticz.Debugging(2)

        Domoticz.Debug("onStart called")
        self.base_topic = Parameters["Mode1"].strip()
        self.pairing_enabled = True if Parameters["Mode2"] == 'true' else False
        self.subscribed_for_devices = False

        mqtt_server_address = Parameters["Address"].strip()
        mqtt_server_port = Parameters["Port"].strip()
        mqtt_client_id = Parameters["Mode3"].strip()
        self.mqttClient = MqttClient(mqtt_server_address, mqtt_server_port, mqtt_client_id, self.onMQTTConnected, self.onMQTTDisconnected, self.onMQTTPublish, self.onMQTTSubscribed)

        self.available_devices = DeviceStorage.getInstance()

    def checkDevices(self):
        Domoticz.Debug("checkDevices called")

    def onStop(self):
        Domoticz.Debug("onStop called")

    def handlePairingMode(self):
        permit_join = 'true' if self.pairing_enabled else 'false'
        self.mqttClient.publish(self.base_topic + '/bridge/config/permit_join', permit_join)

    def onCommand(self, Unit, Command, Level, Color):
        Domoticz.Debug("onCommand: " + Command + ", level (" + str(Level) + ") Color:" + Color)

        device = Devices[Unit] #Devices is Domoticz collection of devices for this hardware
        device_params = device.DeviceID.split('_')
        device_id = device_params[0]
        alias = device_params[1]
        device_data = self.available_devices.get_device_by_id(device_id)

        if (device_data == None):
            Domoticz.Log('Device ' + device.Name + ' does not have registered zigbee2mqtt device')
            return

        model = device_data['model']

        if (model in adapter_by_model):
            adapter = adapter_by_model[model](Devices)
            message = adapter.handleCommand(alias, device, device_data, Command, Level, Color)

            if (message != None):
                self.mqttClient.publish(self.base_topic + '/' + message['topic'], message['payload'])
        else:
            Domoticz.Log('Device ' + device.Name + ' does not have adapter (model: "' + model + '"')
            Domoticz.Log('If you would like plugin to support this device, please create ticket by this link: https://github.com/stas-demydiuk/domoticz-zigbee2mqtt-plugin/issues/new?labels=new+device&template=new-device-support.md')

    def onConnect(self, Connection, Status, Description):
        Domoticz.Debug("onConnect called")
        self.mqttClient.onConnect(Connection, Status, Description)

    def onDisconnect(self, Connection):
        self.mqttClient.onDisconnect(Connection)

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

        if (topic == self.base_topic + '/bridge/config/permit_join' or topic == self.base_topic + '/bridge/config/devices'):
            return

        if (topic == self.base_topic + '/bridge/config'):
            permit_join = 'enabled' if message['permit_join'] else 'disabled'
            Domoticz.Debug('Zigbee2mqtt log level is ' + message['log_level'])
            Domoticz.Log('Joining new devices is ' + permit_join + ' on the zigbee bridge')
            return

        if (topic == self.base_topic + '/bridge/state'):
            Domoticz.Log('Zigbee2mqtt bridge is ' + message)

            if message == 'online':
                self.mqttClient.publish(self.base_topic + '/bridge/config/devices', '')
                self.handlePairingMode()

            return

        if (topic == self.base_topic + '/bridge/log'):
            if message['type'] == 'devices':
                Domoticz.Log('Received available devices list from bridge')
                
                self.available_devices.clear()
                self.available_devices.update(Devices, message['message'])
                
                if self.subscribed_for_devices == False:
                    self.mqttClient.subscribe([self.base_topic + '/+'])
                    self.subscribed_for_devices = True

            if message['type'] == 'device_connected' or message['type'] == 'device_removed':
                self.mqttClient.publish(self.base_topic + '/bridge/config/devices', '')

            return

        device_name = topic.replace(self.base_topic + "/", "")
        device_data = self.available_devices.get_device_by_name(device_name)
        
        if (device_data != None):
            model = device_data['model']

            if (model in adapter_by_model):
                zigbee_message = ZigbeeMessage(message)
                adapter = adapter_by_model[model](Devices)
                adapter.handleMqttMessage(device_data, zigbee_message)
            else:
                Domoticz.Debug('Unsupported zigbee device type with model "' + model + '"')
        else:
            Domoticz.Debug('Unhandled message from zigbee2mqtt: ' + topic + ' ' + str(message))

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
