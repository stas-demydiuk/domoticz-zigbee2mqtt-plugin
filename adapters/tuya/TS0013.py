from adapters.tuya.TS0012 import TS0012
from devices.switch.on_off_switch import OnOffSwitch


class TS0013(TS0012):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(OnOffSwitch(devices, 'center', 'state_left'))

