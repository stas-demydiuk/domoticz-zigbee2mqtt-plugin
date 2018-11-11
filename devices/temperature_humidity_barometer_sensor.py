from decimal import Decimal
import Domoticz
from devices.device import Device


class TemperatureHumidityBarometerSensor(Device):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=84, Subtype=16).Create()

    def get_numeric_value(self, value, device):
        return 0

    def get_string_value(self, value, device):
        return ';'.join([
            str(round(Decimal(value['temperature']), 1)),
            str(value['humidity']),
            '0',  # Humidity status (0 - Normal, 1 - Comfort, 2 - Dry, 3 - Wet)
            str(value['pressure']),
            # Forecast (0 - None, 1 - Sunny, 2 - PartlyCloudy, 3 - Cloudy, 4 - Rain)
            '0'
        ])
