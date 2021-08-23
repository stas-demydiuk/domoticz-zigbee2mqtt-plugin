
from adapters.lumi.aqara_opple_switch import AqaraOppleSwitch


class WXCJKG13LM(AqaraOppleSwitch):
    def __init__(self):
        buttons_count = 6
        super().__init__(buttons_count)
