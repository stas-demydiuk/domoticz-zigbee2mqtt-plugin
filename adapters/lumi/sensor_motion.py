from adapters.base_adapter import Adapter
from devices.motion_sensor import MotionSensor

class SensorMotion(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(MotionSensor(devices, 'motion', 'occupancy'))