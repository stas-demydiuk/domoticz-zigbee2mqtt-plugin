
from adapters.lumi.aqara_opple_switch import AqaraOppleSwitch


class WXCJKG11LM(AqaraOppleSwitch):
    def __init__(self):
        buttons_count = 2
        super().__init__(buttons_count)
