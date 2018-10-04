from adapters.base_adapter import Adapter
from devices.dimmer_switch import DimmerSwitch

class TradfriWirelessDimmer(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(DimmerSwitch(devices, 'brightness', 'brightness'))