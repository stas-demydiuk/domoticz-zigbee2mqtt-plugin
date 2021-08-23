
from adapters.lumi.aqara_opple_switch import AqaraOppleSwitch


class WXCJKG12LM(AqaraOppleSwitch):
    def __init__(self):
        buttons_count = 4
        super().__init__(buttons_count)
