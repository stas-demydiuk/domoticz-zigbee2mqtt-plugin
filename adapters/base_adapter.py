import Domoticz


class Adapter():
    def __init__(self, devices):
        self.devices = []

    def handleMqttMessage(self, message):
        for device in self.devices:
            device.handle_message(message)

    def handleCommand(self, device, command, level, color):
        Domoticz.Log('Update has not been implemented for device "' + device.Name + '"')
