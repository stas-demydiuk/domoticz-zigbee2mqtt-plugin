from adapters.adapter_with_battery import AdapterWithBattery
from devices.temperature_sensor import TemperatureSensor
from devices.humidity_sensor import HumiditySensor


class SensorTemperatureHumidity(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature'))
        self.devices.append(HumiditySensor(devices, 'hum', 'humidity'))
