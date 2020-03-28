from adapters.generic.motion_sensor import MotionSensorAdapter
from devices.sensor.contact import ContactSensor


class SMHMI1(MotionSensorAdapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(ContactSensor(devices, 'tamper', 'tamper'))
