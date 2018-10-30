import Domoticz


class Adapter():
    def __init__(self, devices):
        self.devices = []

    def convert_message(self, message):
        return message

    def register(self, device_data):
        for device in self.devices:
            device.register(device_data)

    def handleMqttMessage(self, device_data, message):
        converted_message = self.convert_message(message)

        for device in self.devices:
            device.handle_message(device_data, converted_message)

    def handleCommand(self, alias, device, device_data, command, level, color):
        Domoticz.Debug('Update command has not been implemented for device "' + device.Name + '"')
