from adapters.base_adapter import Adapter
from devices.water_leak_sensor import WaterLeakSensor

class SensorWleak(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(WaterLeakSensor(devices, 'water_leak', 'water_leak'))