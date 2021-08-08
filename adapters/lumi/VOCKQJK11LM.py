from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.temperature import TemperatureSensor
from devices.sensor.humidity import HumiditySensor
from devices.temperature_humidity_sensor import TemperatureHumiditySensor
from devices.custom_sensor import CustomSensor

class VOCKQJK11LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        # self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', ' (Temperature)'))
        # self.devices.append(HumiditySensor(devices, 'hum', 'humidity', ' (Humidity)'))
        self.devices.append(TemperatureHumiditySensor(devices, 'all', 'combined', ' (Temperature + Humidity)'))
        self.devices.append(CustomSensor(devices, 'voc', 'voc', ' (Voc)'))

    def convert_message(self, message):
        message = super().convert_message(message)
	
        if 'temperature' in message.raw and 'humidity' in message.raw:
            message.raw['combined'] = {
                'temperature': message.raw['temperature'],
                'humidity': message.raw['humidity']
            }

        return message