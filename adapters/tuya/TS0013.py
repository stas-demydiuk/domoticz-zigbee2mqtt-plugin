from adapters.tuya.TS0012 import TS0012
from devices.switch.on_off_switch import OnOffSwitch


class TS0013(TS0012):
    def __init__(self):
        super().__init__()
        self.devices.append(OnOffSwitch('center', 'state_center'))

