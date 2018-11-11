"""
<plugin key="Zigbee2MQTT" name="Zigbee2MQTT" version="0.0.14">
    <description>
      Plugin to add support for <a href="https://github.com/Koenkk/zigbee2mqtt">zigbee2mqtt</a> project<br/><br/>
      Specify MQTT server and port.<br/>
      <br/>
      Automatically creates Domoticz devices for connected device.<br/>
    </description>
    <params>
        <param field="Address" label="MQTT Server address" width="300px" required="true" default="127.0.0.1"/>
        <param field="Port" label="Port" width="300px" required="true" default="1883"/>
        <param field="Mode1" label="Zigbee2Mqtt Topic" width="300px" required="true" default="zigbee2mqtt"/>
        <param field="Mode2" label="Zigbee pairing" width="75px" required="true">
            <options>
                <option label="Enabled" value="true_false"/>
                <option label="Disabled" value="false_true" default="true" />
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
        self.subscribed_for_devices = False

        self.mqttserveraddress = Parameters["Address"].strip()
        self.mqttserverport = Parameters["Port"].strip()
        self.mqttClient = MqttClient(self.mqttserveraddress, self.mqttserverport, self.onMQTTConnected, self.onMQTTDisconnected, self.onMQTTPublish, self.onMQTTSubscribed)

        self.available_devices = DeviceStorage.getInstance()
        
        #set pairing mode of the bridge
        Domoticz.Debug("onStart: set paring mode to :'" + Parameters["Mode2"] + "'")
        self.pairing_atributes = Parameters["Mode2"].split("_")

    def checkDevices(self):
        Domoticz.Debug("checkDevices called")

    def onStop(self):
        Domoticz.Debug("onStop called")

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
                self.mqttClient.Publish(self.base_topic + '/' + message['topic'], message['payload'])
        else:
            Domoticz.Log('Device ' + device.Name + ' does not have adapter (model: "' + model + '"')        

    def onConnect(self, Connection, Status, Description):
        Domoticz.Debug("onConnect called")
        self.mqttClient.onConnect(Connection, Status, Description)

    def onDisconnect(self, Connection):
        self.mqttClient.onDisconnect(Connection)

    def onMessage(self, Connection, Data):
        self.mqttClient.onMessage(Connection, Data)

    def onHeartbeat(self):
        Domoticz.Debug("Heartbeating...")

        # Reconnect if connection has dropped
        if self.mqttClient.mqttConn is None or (not self.mqttClient.mqttConn.Connecting() and not self.mqttClient.mqttConn.Connected() or not self.mqttClient.isConnected):
            Domoticz.Debug("Reconnecting")
            self.mqttClient.Open()
        else:
            self.mqttClient.Ping()

    def onMQTTConnected(self):
        Domoticz.Debug("onMQTTConnected called")
        #Domoticz.Debug("onMQTTConnected: setting bridge pairing mode")
        self.mqttClient.Publish(self.base_topic + '/bridge/config/permit_join', self.pairing_atributes[0])
        #set LED doesn't seem to work.... yet
        self.mqttClient.Publish(self.base_topic + '/bridge/config/disable_led', self.pairing_atributes[1])
        
        self.mqttClient.Subscribe([self.base_topic + '/bridge/#'])

    def onMQTTDisconnected(self):
        Domoticz.Debug("onMQTTDisconnected")

    def onMQTTSubscribed(self):
        Domoticz.Debug("onMQTTSubscribed")

    def onMQTTPublish(self, topic, message):
        Domoticz.Debug("MQTT message: " + topic + " " + str(message))

        if (topic == self.base_topic + '/bridge/state'):
            if message == 'online':
                self.mqttClient.Publish(self.base_topic + '/bridge/config/devices', '')

            Domoticz.Log('Zigbee2mqtt bridge is ' + message)
            return

        if (topic == self.base_topic + '/bridge/log'):
            if message['type'] == 'devices':
                Domoticz.Log('Received available devices list from bridge')
                
                self.available_devices.update(Devices, message['message'])
                
                if self.subscribed_for_devices == False:
                    self.mqttClient.Subscribe([self.base_topic + '/+'])
                    self.subscribed_for_devices = True
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