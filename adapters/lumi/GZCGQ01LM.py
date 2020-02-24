from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.motion import MotionSensor
from devices.sensor.lux import LuxSensor


class GZCGQ01LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(LuxSensor(devices, 'lux', 'illuminance', ' (Illuminance)'))
        self.devices.append(LuxSensor(devices, 'lx', 'illuminance_lux', ' (Illuminance Lux)'))
