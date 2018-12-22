from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.motion import MotionSensor
from devices.lux_sensor import LuxSensor


class SensorMotionAq2(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(MotionSensor(devices, 'motion', 'occupancy'))
        self.devices.append(LuxSensor(devices, 'lux', 'illuminance'))
