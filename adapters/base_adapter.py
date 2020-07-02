import Domoticz
from devices.custom_sensor import CustomSensor


class Adapter():
    def __init__(self, domoticz_devices):
        self.devices = []
        self.devices.append(CustomSensor(domoticz_devices, 'signal', 'linkquality', ' (Link Quality)'))

    def convert_message(self, message):
        return message

    def register(self, device_data):
        for device in self.devices:
            device.register(device_data)

    def remove(self, ieee_addr):
        for device in self.devices:
            device.remove(ieee_addr)

    def get_device_by_alias(self, alias):
        for device in self.devices:
            if device.alias == alias:
                return device

        return None

    def update_link_quality(self, device_data, message):
        if 'linkquality' in message.raw:
            device = self.get_device_by_alias('signal')
            device.handle_message(device_data, message)

    def handleMqttMessage(self, device_data, message):
        converted_message = self.convert_message(message)

        for device in self.devices:
            device.handle_message(device_data, converted_message)

    def handleCommand(self, alias, device, device_data, command, level, color):
        Domoticz.Debug('Update command has not been implemented for device "' + device.Name + '"')
