import Domoticz
from devices.custom_sensor import CustomSensor


class Adapter():
    def __init__(self, devices):
        self.devices = []
        self.devices.append(CustomSensor(devices, 'signal', 'linkquality', ' (Link Quality)'))

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

    def remove(self):
        pass