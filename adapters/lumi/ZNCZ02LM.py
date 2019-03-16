from adapters.lumi.plug import Plug
from devices.sensor.temperature import TemperatureSensor

# Xiaomi Mi power plug
class ZNCZ02KM(Plug):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', ' (Temperature)'))
