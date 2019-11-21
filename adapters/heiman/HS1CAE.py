from adapters.base_adapter import Adapter
from devices.sensor.smoke import SmokeSensor

class HS1CAE(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(SmokeSensor(devices, 'co', 'carbon_monoxide'))
