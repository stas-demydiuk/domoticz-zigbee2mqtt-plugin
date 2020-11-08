import domoticz
from devices.custom_sensor import CustomSensor


class Adapter():
    def __init__(self, domoticz_devices):
        self.devices = []

        if domoticz.get_plugin_config('trackLinkQuality'):
            self.devices.append(CustomSensor(domoticz_devices, 'signal', 'linkquality', ' (Link Quality)'))

    def convert_message(self, message):
        return message

    def _get_legacy_device_data(self):
        if 'type' not in self.zigbee_device:
            domoticz.error(self.name + ': device does not contain type')
            return

        if 'model' not in self.zigbee_device['definition']:
            domoticz.error(self.name + ': device definiton does not contain model')
            return

        return {
            'type': self.zigbee_device['type'],
            'model': self.zigbee_device['definition']['model'],
            'ieee_addr': self.zigbee_device['ieee_address'],
            'friendly_name': self.name
        }

    def register(self):
        for device in self.devices:
            device.register(self._get_legacy_device_data())

    def remove(self, ieee_addr):
        for device in self.devices:
            device.remove(ieee_addr)

    def get_device_by_alias(self, alias):
        for device in self.devices:
            if device.alias == alias:
                return device

        return None

    def update_link_quality(self, device_data, message):
        config = domoticz.get_plugin_config()
        if config["trackLinkQuality"] == False:
            return None

        if 'linkquality' in message.raw:
            device = self.get_device_by_alias('signal')
            device.handle_message(device_data, message)

    def handle_mqtt_message(self, message):
        converted_message = self.convert_message(message)
        device_data = self._get_legacy_device_data()

        if (device_data == None):
            domoticz.debug(self.name + ': not enough details to handle MQTT message from device')
            return

        for device in self.devices:
            device.handle_message(device_data, converted_message)

    def handle_command(self, alias, device, command, level, color):
        domoticz.debug('Update command has not been implemented for device "' + device.Name + '"')
