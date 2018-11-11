from decimal import Decimal
import Domoticz
from devices.device import Device


class TemperatureHumiditySensor(Device):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Temp+Hum").Create()

    def get_numeric_value(self, value, device):
        return 0

    def get_string_value(self, value, device):
        return ';'.join([
            str(round(Decimal(value['temperature']), 1)),
            str(value['humidity']),
            '0'  # Humidity status (0 - Normal, 1 - Comfort, 2 - Dry, 3 - Wet)
        ])
