from adapters.generic.plug import PlugAdapter
from devices.sensor.temperature import TemperatureSensor


class ZNCZ04LM(PlugAdapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', ' (Temperature)'))

