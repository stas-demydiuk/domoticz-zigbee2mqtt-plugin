from adapters.adapter_with_battery import AdapterWithBattery
from devices.temperature_sensor import TemperatureSensor
from devices.humidity_sensor import HumiditySensor
from devices.temperature_humidity_sensor import TemperatureHumiditySensor


class SensorTemperatureHumidity(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', ' (Temperature)'))
        self.devices.append(HumiditySensor(devices, 'hum', 'humidity', ' (Humidity)'))
        self.devices.append(TemperatureHumiditySensor(devices, 'all', 'combined', ' (Temperature + Humidity)'))

    def convert_message(self, message):
        message = super().convert_message(message)
	
        if 'temperature' in message.raw and 'humidity' in message.raw:
            message.raw['combined'] = ';'.join([
                str(message.raw['temperature']),
                str(message.raw['humidity']),
                '0' # Humidity status (0 - Normal, 1 - Comfort, 2 - Dry, 3 - Wet)
            ])

        return message
