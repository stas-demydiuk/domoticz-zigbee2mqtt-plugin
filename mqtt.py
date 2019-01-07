# Based on https://github.com/emontnemery/domoticz_mqtt_discovery
import Domoticz
import time
import json
import random


class MqttClient:
    Address = ""
    Port = ""
    mqttConn = None
    isConnected = False
    mqttConnectedCb = None
    mqttDisconnectedCb = None
    mqttPublishCb = None

    def __init__(self, destination, port, clientId, mqttConnectedCb, mqttDisconnectedCb, mqttPublishCb, mqttSubackCb):
        Domoticz.Debug("MqttClient::__init__")
        
        self.address = destination
        self.port = port
        self.client_id = clientId if clientId != "" else 'Domoticz_'+str(int(time.time()))+'_'+str(random.randint(1000, 9999))
        self.mqttConnectedCb = mqttConnectedCb
        self.mqttDisconnectedCb = mqttDisconnectedCb
        self.mqttPublishCb = mqttPublishCb
        self.mqttSubackCb = mqttSubackCb
        self.Open()

    def __str__(self):
        Domoticz.Debug("MqttClient::__str__")
        if (self.mqttConn != None):
            return str(self.mqttConn)
        else:
            return "None"

    def Open(self):
        Domoticz.Debug("MqttClient::Open")
        if (self.mqttConn != None):
            self.Close()
        self.isConnected = False

        protocol = "MQTTS" if self.port == "8883" else "MQTT"

        self.mqttConn = Domoticz.Connection(Name=self.address, Transport="TCP/IP", Protocol=protocol, Address=self.address, Port=self.port)
        self.mqttConn.Connect()

    def Connect(self):
        Domoticz.Debug("MqttClient::Connect")
        if (self.mqttConn == None):
            self.Open()
        else:
            Domoticz.Debug("MQTT CONNECT ID: '" + self.client_id + "'")
            self.mqttConn.Send({'Verb': 'CONNECT', 'ID': self.client_id})

    def Ping(self):
        Domoticz.Debug("MqttClient::Ping")
        if (self.mqttConn == None or not self.isConnected):
            self.Open()
        else:
            self.mqttConn.Send({'Verb': 'PING'})

    def Publish(self, topic, payload, retain = 0):
        Domoticz.Debug("MqttClient::Publish " + topic + " (" + payload + ")")
        if (self.mqttConn == None or not self.isConnected):
            self.Open()
        else:
            self.mqttConn.Send({'Verb': 'PUBLISH', 'Topic': topic, 'Payload': bytearray(payload, 'utf-8'), 'Retain': retain})

    def Subscribe(self, topics):
        Domoticz.Debug("MqttClient::Subscribe")
        subscriptionlist = []
        for topic in topics:
            subscriptionlist.append({'Topic':topic, 'QoS':0})
        if (self.mqttConn == None or not self.isConnected):
            self.Open()
        else:
            self.mqttConn.Send({'Verb': 'SUBSCRIBE', 'Topics': subscriptionlist})

    def Close(self):
        Domoticz.Debug("MqttClient::Close")
        #TODO: Disconnect from server
        self.mqttConn = None
        self.isConnected = False

    def onConnect(self, Connection, Status, Description):
        if (Status == 0):
            Domoticz.Debug("MQTT connected successfully.")
            self.Connect()
        else:
            Domoticz.Log("Failed to connect to: " + Connection.Address + ":" + Connection.Port + ", Description: " + Description)

    def onDisconnect(self, Connection):
        Domoticz.Debug("MqttClient::onDisonnect Disconnected from: " + Connection.Address+":" + Connection.Port)
        self.Close()
        # TODO: Reconnect?
        if self.mqttDisconnectedCb != None:
            self.mqttDisconnectedCb()

    def onHeartbeat(self):
        if self.mqttConn is None or (not self.mqttConn.Connecting() and not self.mqttConn.Connected() or not self.isConnected):
            Domoticz.Debug("MqttClient::Reconnecting")
            self.Open()
        else:
            self.Ping()

    def onMessage(self, Connection, Data):
        topic = ''
        if 'Topic' in Data:
            topic = Data['Topic']
        payloadStr = ''
        if 'Payload' in Data:
            payloadStr = Data['Payload'].decode('utf8','replace')
            payloadStr = str(payloadStr.encode('unicode_escape'))

        if Data['Verb'] == "CONNACK":
            self.isConnected = True
            if self.mqttConnectedCb != None:
                self.mqttConnectedCb()

        if Data['Verb'] == "SUBACK":
            if self.mqttSubackCb != None:
                self.mqttSubackCb()

        if Data['Verb'] == "PUBLISH":
            if self.mqttPublishCb != None:
                rawmessage = Data['Payload'].decode('utf8')
                message = ""

                try:
                    message = json.loads(rawmessage)
                except ValueError:
                    message = rawmessage
                    
                self.mqttPublishCb(topic, message)