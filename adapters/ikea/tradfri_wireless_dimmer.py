from adapters.base_adapter import Adapter
from devices.switch.dimmer_switch import DimmerSwitch

class TradfriWirelessDimmer(Adapter):
    def __init__(self):
        super().__init__()
        self.devices.append(DimmerSwitch('dimmer', 'brightness'))