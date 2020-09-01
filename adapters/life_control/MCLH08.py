from adapters.base_adapter import Adapter
from devices.sensor.co2 import CO2Sensor
from devices.sensor.temperature import TemperatureSensor
from devices.sensor.humidity import HumiditySensor
from devices.temperature_humidity_sensor import TemperatureHumiditySensor
from devices.custom_sensor import CustomSensor

class MCLH08(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', ' (Temperature)'))
        self.devices.append(HumiditySensor(devices, 'hum', 'humidity', ' (Humidity)'))
        self.devices.append(TemperatureHumiditySensor(devices, 'all', 'combined', ' (Temperature + Humidity)'))
        self.devices.append(CO2Sensor(devices, 'eco2', 'eco2', ' (CO2)'))
        self.devices.append(CustomSensor(devices, 'voc', 'voc', ' (Vok)'))

    def convert_message(self, message):
        message = super().convert_message(message)
	
        if 'temperature' in message.raw and 'humidity' in message.raw:
            message.raw['combined'] = {
                'temperature': message.raw['temperature'],
                'humidity': message.raw['humidity']
            }

        return message