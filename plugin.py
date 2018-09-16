"""
<plugin key="Zigbee2MQTT" name="Zigbee2MQTT" version="0.0.1">
    <description>
      Plugin to add support for <a href="https://github.com/Koenkk/zigbee2mqtt">zigbee2mqtt</a> project<br/><br/>
      Specify MQTT server and port.<br/>
      <br/>
      Automatically creates Domoticz devices for connected device.<br/>
    </description>
    <params>
        <param field="Address" label="MQTT Server address" width="300px" required="true" default="127.0.0.1"/>
        <param field="Port" label="Port" width="300px" required="true" default="1883"/>

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
from adapters.lumi.sensor_cube import SensorCube
from adapters.lumi.sensor_86sw2 import Sensor86Sw2
from adapters.lumi.sensor_wleak import SensorWleak
from adapters.lumi.plug import Plug
from adapters.lumi.ctrl_neutral2 import AqaraDoubleWiredSwitch

class BasePlugin:
    mqttClient = None

    def onStart(self):
        self.debugging = Parameters["Mode6"]
        
        if self.debugging == "Verbose":
            Domoticz.Debugging(2+4+8+16+64)
        if self.debugging == "Debug":
            Domoticz.Debugging(2)

        self.base_topic = 'zigbee2mqtt/'
        self.topics = list([self.base_topic + '+'])

        self.mqttserveraddress = Parameters["Address"].strip()
        self.mqttserverport = Parameters["Port"].strip()
        self.mqttClient = MqttClient(self.mqttserveraddress, self.mqttserverport, self.onMQTTConnected, self.onMQTTDisconnected, self.onMQTTPublish, self.onMQTTSubscribed)

        self.adapter_by_model = {
            'lumi.plug': Plug,
            'lumi.sensor_cube': SensorCube,
            'lumi.sensor_86sw2.es1': Sensor86Sw2,
            'lumi.sensor_86sw2\x00Un': Sensor86Sw2,
            'lumi.sensor_wleak.aq1': SensorWleak,
            'lumi.ctrl_neutral2': AqaraDoubleWiredSwitch
        }

    def checkDevices(self):
        Domoticz.Debug("checkDevices called")

    def onStop(self):
        Domoticz.Debug("onStop called")

    def onCommand(self, Unit, Command, Level, Color):
        Domoticz.Debug("Command: " + Command + " (" + str(Level) + ") Color:" + Color)

        device = Devices[Unit]

        if ('model' not in device.Options):
            Domoticz.Log('Device ' + device.Name + ' does not have saved model')
            return

        modelId = device.Options['model']
        
        if (modelId in self.adapter_by_model):
            adapter = self.adapter_by_model[modelId](Devices)
            message = adapter.handleCommand(device, Command, Level, Color)

            if (message == None):
                Domoticz.Log('Device ' + device.Name + ' does not support command')
                return

            self.mqttClient.Publish(self.base_topic + message['topic'], message['payload'])
        else:
            Domoticz.Log('Device ' + device.Name + ' does not have adapter')

    def onConnect(self, Connection, Status, Description):
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
        Domoticz.Debug("onMQTTConnected")
        self.mqttClient.Subscribe(self.topics)

    def onMQTTDisconnected(self):
        Domoticz.Debug("onMQTTDisconnected")

    def onMQTTSubscribed(self):
        Domoticz.Debug("onMQTTSubscribed")

    def onMQTTPublish(self, topic, message):
        Domoticz.Debug("MQTT message: " + topic + " " + str(message))
        zigbee_message = ZigbeeMessage(message)
        model = zigbee_message.get_device_model()

        if (model in self.adapter_by_model):
            adapter = self.adapter_by_model[model](Devices)
            adapter.handleMqttMessage(zigbee_message)
        else:
            Domoticz.Debug('Unsupported zigbee device type with model ' + model)

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