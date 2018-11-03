from adapters.adapter_with_battery import AdapterWithBattery
from devices.motion_sensor import MotionSensor


class SensorMotion(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(MotionSensor(devices, 'motion', 'occupancy'))
