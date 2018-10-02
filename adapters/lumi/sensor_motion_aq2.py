from adapters.base_adapter import Adapter
from devices.motion_sensor import MotionSensor
from devices.lux_sensor import LuxSensor

class SensorMotionAq2(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(MotionSensor(devices, 'motion', 'occupancy'))
        self.devices.append(LuxSensor(devices, 'lux', 'illuminance'))