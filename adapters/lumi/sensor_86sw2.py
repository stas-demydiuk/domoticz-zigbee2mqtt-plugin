from adapters.base_adapter import Adapter
from devices.selector_switch import SelectorSwitch


class Sensor86Sw2(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        switch = SelectorSwitch(devices, 'switch', 'click')
        switch.add_level('Off', None)
        switch.add_level('Switch 1', 'left')
        switch.add_level('Switch 2', 'right')
        switch.add_level('Both_Click', 'both')
        switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)

        self.devices.append(switch)
