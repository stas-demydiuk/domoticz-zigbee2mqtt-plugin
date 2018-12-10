from adapters.adapter_with_battery import AdapterWithBattery
from devices.temperature_sensor import TemperatureSensor
from devices.humidity_sensor import HumiditySensor
from devices.pressure_sensor import PressureSensor
from devices.temperature_humidity_sensor import TemperatureHumiditySensor
from devices.temperature_humidity_barometer_sensor import TemperatureHumidityBarometerSensor


# Xiaomi Aqara temperature, humidity and pressure sensor 
class WSDCGQ11LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', ' (Temperature)'))
        self.devices.append(HumiditySensor(devices, 'hum', 'humidity', ' (Humidity)'))
        self.devices.append(PressureSensor(devices, 'pres', 'pressure', ' (Pressure)'))
        self.devices.append(TemperatureHumiditySensor(devices, 'th', 'combined', ' (Temperature + Humidity)'))
        self.devices.append(TemperatureHumidityBarometerSensor(devices, 'all', 'combined', ' (Temperature + Humidity + Barometer)'))

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'temperature' in message.raw and 'humidity' in message.raw and 'pressure' in message.raw:
            message.raw['combined'] = {
                'temperature': message.raw['temperature'],
                'humidity': message.raw['humidity'],
                'pressure': message.raw['pressure']
            }

        return message
