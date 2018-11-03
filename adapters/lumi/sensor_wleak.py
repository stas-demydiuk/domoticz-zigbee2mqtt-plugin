from adapters.adapter_with_battery import AdapterWithBattery
from devices.water_leak_sensor import WaterLeakSensor


class SensorWleak(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(WaterLeakSensor(devices, 'wleak', 'water_leak'))
