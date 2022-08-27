"""
<plugin key="Zigbee2MQTT" name="Zigbee2MQTT" version="3.2.0-beta">
    <description>
        <h2>Zigbee2MQTT Plugin (v. 3.2.0-beta)</h2>
        <p>Plugin to add support for <a href="https://github.com/Koenkk/zigbee2mqtt">zigbee2mqtt</a> project</p>
        <h3>Features</h3>
        <ul style="list-style-type:square">
            <li>Allows to manage and control zigbee devices</li>
            <li>Allows to manage and control zigbee groups</li>
            <li>Custom UI page to improve user experience</li>
            <li>Zigbee network map visualization</li>
        </ul>
        <h3>Blacklist</h3>
        <p>Plugin allows to skip processing of some devices by adding them to the blacklist. Blacklisted devices will ot be created as logical devices in Domoticz.</p>
        <p>Blacklist could contain several entries devided by semi-colon. Each blacklist entry should be valid <a href="https://docs.python.org/3/library/re.html#regular-expression-syntax">Python regexp</a>. For example:</p>
        <ul style="list-style-type:square">
            <li>Single feature of a device - use full Device Address + '_' + Feature Name pattern to block it i.e. <span class="label label-default">0x842e14fffe13971a_state</span></li>
            <li>All items of a device - use Regexp to block all logical devices (aliases) of a specified zigbee device (ieee address) i.e. <span class="label label-default">0x842e14fffe13971a_.*</span></li>
            <li>Specific item of all devices - use Regexp to block all devices (ieee address) with a specific alias i.e. <span class="label label-default">.*_state</span></li>
        </ul>
    </description>
    <params>
        <param field="Address" label="MQTT Server address" width="300px" required="true" default="127.0.0.1"/>
        <param field="Port" label="Port" width="300px" required="true" default="1883"/>
        <param field="Username" label="MQTT Username (optional)" width="300px" required="false" default=""/>
        <param field="Password" label="MQTT Password (optional)" width="300px" required="false" default="" password="true"/>
        <param field="Mode3" label="MQTT Client ID (optional)" width="300px" required="false" default=""/>
        <param field="Mode1" label="Zigbee2Mqtt Topic" width="300px" required="true" default="zigbee2mqtt"/>
        <param field="Mode2" label="Devices Blacklist" width="100%" required="false" default=""/>
        <param field="Mode4" label="Track Link Quality" width="300px">
            <options>
                <option label="Yes" value="Yes" default="true"/>
                <option label="No" value="No" />
            </options>
        </param>
        <param field="Mode5" label="Use Battery Devices" width="300px">
            <options>
                <option label="Yes" value="Yes" default="true"/>
                <option label="No" value="No" />
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
import DomoticzEx as Domoticz
import domoticz
import bridge
import os
from shutil import copy2, rmtree
from mqtt import MqttClient
from api import API
import configuration
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

        self.install()
        self.base_topic = Parameters["Mode1"].strip()

        mqtt_server_address = Parameters["Address"].strip()
        mqtt_server_port = Parameters["Port"].strip()
        mqtt_client_id = Parameters["Mode3"].strip()
        self.mqttClient = MqttClient(mqtt_server_address, mqtt_server_port, mqtt_client_id, self.onMQTTConnected, self.onMQTTDisconnected, self.onMQTTPublish, self.onMQTTSubscribed)

        self.api = API(self.onApiCommand)
        self.devices_manager = DevicesManager()
        self.groups_manager = GroupsManager()

    def checkDevices(self):
        domoticz.debug("checkDevices called")

    def onStop(self):
        domoticz.debug("onStop called")
        self.uninstall()


    def onCommand(self, device_id, unit, command, Level, Color):
        domoticz.debug("[Command] Device " + device_id + '(' + str(unit) + '): ' + command + "(level = " + str(Level) + ", color = " + Color + ')')

        message = None
        domoticz_device = domoticz.get_device(device_id, unit)
        zigbee_device_alias = configuration.get_zigbee_feature_data(device_id, unit)
        
        if zigbee_device_alias == None:
            domoticz.log('Can\'t process command from device "' + domoticz_device.Name + '"')

        if self.groups_manager.get_group_by_id(zigbee_device_alias['zigbee']['address']) != None:
            message = self.groups_manager.handle_command(device_id, unit, command, Level, Color)
        else:
            message = self.devices_manager.handle_command(device_id, unit, command, Level, Color)

        if (message != None):
            self.publishToMqtt(message['topic'], message['payload'])

    def onApiCommand(self, command, data):
        if command == 'publish_mqtt':
            return self.publishToMqtt(data['topic'], data['payload'])
        elif command == 'remove_device':
            return self.devices_manager.remove(data)
        else:
            domoticz.error('Internal API command "' + command +'" is not supported by plugin')

    def publishToMqtt(self, topic, payload):
        self.mqttClient.publish(self.base_topic + '/' + topic, payload)

    def onConnect(self, Connection, Status, Description):
        domoticz.debug("onConnect called")
        self.mqttClient.onConnect(Connection, Status, Description)

    def onDisconnect(self, Connection):
        self.mqttClient.onDisconnect(Connection)

    def onDeviceModified(self, device_id, unit):
        if device_id == 'api_transport' and unit == 255:
            device = domoticz.get_device(device_id, unit)
            self.api.handle_request(device.sValue)
            return

    def onMessage(self, Connection, Data):
        self.mqttClient.onMessage(Connection, Data)

    def onHeartbeat(self):
        self.mqttClient.onHeartbeat()

    def onMQTTConnected(self):
        self.mqttClient.subscribe([self.base_topic + '/#'])

    def onMQTTDisconnected(self):
        domoticz.debug('Disconnected from MQTT server')

    def onMQTTSubscribed(self):
        domoticz.debug('Subscribed to "' + self.base_topic + '/#" topic')

    def onMQTTPublish(self, topic, message):
        # domoticz.debug("MQTT message: " + topic + " " + str(message))
        topic = topic.replace(self.base_topic + '/', '')

        self.api.handle_mqtt_message(topic, message)
        bridge.handle_mqtt_message(topic, message)

        if (topic == 'bridge/config/permit_join'):
            return

        if (topic == 'bridge/config/logging') or (topic == 'bridge/logging'):
            # TODO: Add log feature
            return

        if (topic == 'bridge/devices'):
            self.devices_manager.set_devices(message)
            return

        if (topic == 'bridge/groups'):
            self.groups_manager.register_groups(message)
            return

        if (topic == 'bridge/config'):
            permit_join = 'enabled' if message['permit_join'] else 'disabled'
            domoticz.debug('Zigbee2mqtt log level is ' + message['log_level'])
            domoticz.log('Joining new devices is ' + permit_join + ' on the zigbee bridge')
            return

        if (topic == 'bridge/state'):
            bridge_status = str(message['state']) if type(message) is dict else str(message)
            domoticz.log('Zigbee2mqtt bridge is ' + bridge_status)
            return

        if (topic == 'bridge/log'):
            is_connected = message['type'] == 'device_connected'
            is_removed = message['type'] == 'device_removed'
            is_paired = message['type'] == 'pairing' and message['message'] == 'interview_successful'

            if is_connected or is_removed or is_paired:
                self.publishToMqtt('bridge/config/devices/get', '')

            if message['type'] == 'ota_update':
                domoticz.log(message['message'])

            if (message['type'] == 'device_renamed'):
                domoticz.debug("Device renamed from '{0}' to '{1}'".format(message['message']['from'], message['message']['to']))
                if (self.devices_manager.get_device_by_name(message['message']['from']) != None):
                    domoticz.debug("attempt to rename on bridge/log")
                    toRename = self.devices_manager.get_device_by_name(message['message']['from'])
                    toRename.zigbee_device['friendly_name'] = message['message']['to']
                    self.devices_manager.devices[toRename.zigbee_device['ieee_address']] = toRename
                else:
                    domoticz.debug("attempt to rename failed on bridge/log")
                
            if message['type'] == 'zigbee_publish_error':
                #an error occured on publish to the zigbee network
                deviceMeta = message['meta']
                domoticz.error("A Zigbee publish error occured for device '" + deviceMeta['friendly_name'] + "' with error message: " + message['message'])

            return

        if (self.groups_manager.get_group_by_name(topic) != None):
            self.groups_manager.handle_mqtt_message(topic, message)
        elif (self.devices_manager.get_device_by_name(topic) != None):
            self.devices_manager.handle_mqtt_message(topic, message)

    def install(self):
        domoticz.log('Installing plugin custom page...')

        try:
            source_path = Parameters['HomeFolder'] + 'frontend'
            templates_path = Parameters['StartupFolder'] + 'www/templates'
            dst_plugin_path = templates_path + '/zigbee2mqtt'

            domoticz.debug('Copying files from ' + source_path + ' to ' + templates_path)

            if not (os.path.isdir(dst_plugin_path)):
                os.makedirs(dst_plugin_path)

            copy2(source_path + '/zigbee2mqtt.html', templates_path)
            copy2(source_path + '/zigbee2mqtt.js', templates_path)
            copy2(source_path + '/plugin_config.js', dst_plugin_path)
            copy2(source_path + '/zigbee_devices.js', dst_plugin_path)
            copy2(source_path + '/zigbee_groups.js', dst_plugin_path)
            copy2(source_path + '/libs/leaflet.js', dst_plugin_path)
            copy2(source_path + '/libs/leaflet.css', dst_plugin_path)
            copy2(source_path + '/libs/viz.js', dst_plugin_path)
            copy2(source_path + '/libs/viz.full.render.js', dst_plugin_path)
            copy2(source_path + '/libs/ace_json_mode.js', dst_plugin_path)
            copy2(source_path + '/libs/ace_worker_json.js', dst_plugin_path)
            
            domoticz.log('Installing plugin custom page completed.')
        except Exception as e:
            domoticz.error('Error during installing plugin custom page')
            domoticz.error(repr(e))

    def uninstall(self):
        domoticz.log('Uninstalling plugin custom page...')

        try:
            templates_path = Parameters['StartupFolder'] + 'www/templates'
            dst_plugin_path = templates_path + '/zigbee2mqtt'

            domoticz.debug('Removing files from ' + templates_path)

            if (os.path.isdir(dst_plugin_path)):
                rmtree(dst_plugin_path)

            if os.path.exists(templates_path + "/zigbee2mqtt.html"):
                os.remove(templates_path + "/zigbee2mqtt.html")

            if os.path.exists(templates_path + "/zigbee2mqtt.js"):
                os.remove(templates_path + "/zigbee2mqtt.js")

            domoticz.log('Uninstalling plugin custom page completed.')
        except Exception as e:
            domoticz.error('Error during uninstalling plugin custom page')
            domoticz.error(repr(e))


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

def onDeviceModified(DeviceId, Unit):
    global _plugin
    _plugin.onDeviceModified(DeviceId, Unit)

def onDeviceRemoved(DeviceId, Unit):
    configuration.remove_device(DeviceId, Unit)

def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)

def onMessage(Connection, Data):
    global _plugin
    _plugin.onMessage(Connection, Data)

def onCommand(DeviceId, Unit, Command, Level, Color):
    global _plugin
    _plugin.onCommand(DeviceId, Unit, Command, Level, Color)

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()
