from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from devices.sensor.contact import ContactSensor


class HS1WLE(WaterLeakSensorAdapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(ContactSensor(devices, 'tamper', 'tamper'))
