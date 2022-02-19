import domoticz
from devices.device import Device


class BarometerSensor(Device):
    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Barometer")

    def get_numeric_value(self, value, device):
        return 0

    def get_string_value(self, value, device):
        return ';'.join([
            str(value),
            str(self.get_forecast(value))
        ])

    def get_forecast(self, value):
        # Forecast is based on https://github.com/stas-demydiuk/domoticz-zigbee2mqtt-plugin/issues/102

        if (value < 996):
            return 4  # Thunderstorm
        elif (value < 993):
            return 3  # Not stable
        elif (value < 1007):
            return 2  # Cloudy/Rain
        elif (value < 1013):
            return 1  # Clear/Sunny
        elif (value < 1033):
            return 0  # Stable
        else:
            return 5  # Unknown
