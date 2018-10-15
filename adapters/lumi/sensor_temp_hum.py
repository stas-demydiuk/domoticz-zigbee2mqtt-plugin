from adapters.base_adapter import Adapter
from devices.temperature_sensor import TemperatureSensor
from devices.humidity_sensor import HumiditySensor


class SensorTemperatureHumidity(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature'))
        self.devices.append(HumiditySensor(devices, 'hum', 'humidity'))
