
from adapters.lumi.aqara_opple_switch import AqaraOppleSwitch
from devices.switch.selector_switch import SelectorSwitch


class WXCJKG13LM(AqaraOppleSwitch):
    def __init__(self, devices):
        buttons_count = 6
        super().__init__(devices, buttons_count)
