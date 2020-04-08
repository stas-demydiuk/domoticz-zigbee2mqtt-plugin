from adapters.contact_adapter import ContactAdapter
from devices.sensor.contact import ContactSensor


class AV201021(ContactAdapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(ContactSensor(devices, 'tamper', 'tamper'))
