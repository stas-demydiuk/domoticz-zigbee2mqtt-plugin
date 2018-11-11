from adapters.adapter_with_battery import AdapterWithBattery
from devices.temperature_sensor import TemperatureSensor
from devices.humidity_sensor import HumiditySensor
from devices.pressure_sensor import PressureSensor
from devices.temperature_humidity_barometer_sensor import TemperatureHumidityBarometerSensor


class Weather(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', ' (Temperature)'))
        self.devices.append(HumiditySensor(devices, 'hum', 'humidity', ' (Humidity)'))
        self.devices.append(PressureSensor(devices, 'pres', 'pressure', ' (Pressure)'))
        self.devices.append(TemperatureHumidityBarometerSensor(devices, 'all', 'combined', ' (Temperature + Humidity + Barometer)'))

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'temperature' in message.raw and 'humidity' in message.raw and 'pressure' in message.raw:
            message.raw['combined'] = ';'.join([
                str(message.raw['temperature']),
                str(message.raw['humidity']),
                '0', # Humidity status (0 - Normal, 1 - Comfort, 2 - Dry, 3 - Wet)
                str(message.raw['pressure']),
                '0' # Forecast (0 - None, 1 - Sunny, 2 - PartlyCloudy, 3 - Cloudy, 4 - Rain)
            ])

        return message
