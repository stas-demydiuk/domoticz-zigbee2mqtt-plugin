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
from mqtt import MqttClient
from adopters.aqara_cube import AqaraCube
from adopters.sensor_86sw2 import Sensor86Sw2

class BasePlugin:
    mqttClient = None

    def onStart(self):
        self.debugging = Parameters["Mode6"]
        
        if self.debugging == "Verbose":
            Domoticz.Debugging(2+4+8+16+64)
        if self.debugging == "Debug":
            Domoticz.Debugging(2)

        self.topics = list(["zigbee2mqtt/+"])

        self.mqttserveraddress = Parameters["Address"].replace(" ", "")
        self.mqttserverport = Parameters["Port"].replace(" ", "")
        self.mqttClient = MqttClient(self.mqttserveraddress, self.mqttserverport, self.onMQTTConnected, self.onMQTTDisconnected, self.onMQTTPublish, self.onMQTTSubscribed)

    def checkDevices(self):
        Domoticz.Debug("checkDevices called")

    def onStop(self):
        Domoticz.Debug("onStop called")

    def onCommand(self, Unit, Command, Level, Color):
        Domoticz.Debug("Command: " + Command + " (" + str(Level) + ") Color:" + Color)
        # self.controller.onCommand(self.mqttClient, Unit, Command, Level, Color)

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

        modelId = message['device']['modelId']

        if (modelId == 'lumi.sensor_cube'):
            controller = AqaraCube(Devices)
            controller.handleMqttMessage(message)
        elif (modelId == 'lumi.sensor_86sw2\x00Un' or modelId == 'lumi.sensor_86sw2.es1'):
            controller = Sensor86Sw2(Devices)
            controller.handleMqttMessage(message)

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