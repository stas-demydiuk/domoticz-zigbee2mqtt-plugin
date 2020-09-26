from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch

class WXKG07LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Left Click', 'left')
        self.switch.add_level('Left Double Click', 'left_double')
        self.switch.add_level('Left Long Click', 'left_long')
        self.switch.add_level('Right Click', 'right')
        self.switch.add_level('Right Double Click', 'right_double')
        self.switch.add_level('Right Long Click', 'right_long')
        self.switch.add_level('Both Click', 'both')
        self.switch.add_level('Both Double Click', 'both_double')
        self.switch.add_level('Both Long Click', 'both_long')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.switch.disable_value_check_on_update()

        self.devices.append(self.switch)
