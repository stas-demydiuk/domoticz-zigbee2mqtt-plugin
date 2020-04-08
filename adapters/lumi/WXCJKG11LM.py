
from adapters.lumi.aqara_opple_switch import AqaraOppleSwitch


class WXCJKG11LM(AqaraOppleSwitch):
    def __init__(self, devices):
        buttons_count = 2
        super().__init__(devices, buttons_count)
