from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.motion import MotionSensor


class MotionSensorAdapter(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(MotionSensor(devices, 'motion', 'occupancy'))
