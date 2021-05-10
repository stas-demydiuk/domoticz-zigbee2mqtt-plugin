from decimal import Decimal
import Domoticz
from devices.temperature_humidity_sensor import TemperatureHumiditySensor


class TemperatureHumidityBarometerSensor(TemperatureHumiditySensor):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=84, Subtype=16).Create()

    def set_pressure_feature(self, feature):
        self.pressure_feature = feature

    def get_pressure_value(self, value):
        if hasattr(self, 'pressure_feature'):
            value = value[self.pressure_feature['property']]
        else:
            value = value['pressure']

        return str(value)

    def get_string_value(self, value, device):
        return ';'.join([
            self.get_temperature_value(value),
            self.get_humidity_value(value),
            self.get_humidity_status(value),
            self.get_pressure_value(value),
            # Forecast (0 - None, 1 - Sunny, 2 - PartlyCloudy, 3 - Cloudy, 4 - Rain)
            str(self.get_forecast(value['pressure']))
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
