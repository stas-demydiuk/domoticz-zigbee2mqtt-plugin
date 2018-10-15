import Domoticz


class Adapter():
    def __init__(self, devices):
        self.devices = []

    def handleMqttMessage(self, device_data, message):
        for device in self.devices:
            device.handle_message(device_data, message)

    def handleCommand(self, alias, device, device_data, command, level, color):
        Domoticz.Debug('Update command has not been implemented for device "' + device.Name + '"')
