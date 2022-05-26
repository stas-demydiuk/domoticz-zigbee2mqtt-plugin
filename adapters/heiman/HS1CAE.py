from adapters.base_adapter import Adapter
from devices.sensor.smoke import SmokeSensor

class HS1CAE(Adapter):
    def __init__(self):
        super().__init__()
        self.devices.append(SmokeSensor('co', 'carbon_monoxide'))
