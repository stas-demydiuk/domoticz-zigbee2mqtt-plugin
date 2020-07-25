from adapters.generic.gas_sensor import GasSensorAdapter
from devices.sensor.contact import ContactSensor

class CrGasSensorAdapter(GasSensorAdapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(ContactSensor(devices, 'tamper', 'tamper'))
