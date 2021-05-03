from decimal import Decimal
import Domoticz
from devices.device import Device


class TemperatureHumiditySensor(Device):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Temp+Hum").Create()

    def set_temp_feature(self, feature):
        self.temp_feature = feature

    def set_humidity_feature(self, feature):
        self.humidity_feature = feature

    def get_message_value(self, message):
        return message.raw

    def get_numeric_value(self, value, device):
        return 0

    def get_temperature_value(self, value):
        if hasattr(self, 'temp_feature'):
            value = value[self.temp_feature['property']]
        else:
            value = value['temperature']

        return str(round(Decimal(value), 1))

    def get_humidity_value(self, value):
        if hasattr(self, 'humidity_feature'):
            value = value[self.humidity_feature['property']]
        else:
            value = value['humidity']

        return str(value)

    def get_humidity_status(self, value):
        # Humidity status (0 - Normal, 1 - Comfort, 2 - Dry, 3 - Wet)
        return '0'

    def get_string_value(self, value, device):
        return ';'.join([
            self.get_temperature_value(value),
            self.get_humidity_value(value),
            self.get_humidity_status(value)
        ])
