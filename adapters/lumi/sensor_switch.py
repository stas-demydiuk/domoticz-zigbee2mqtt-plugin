from adapters.base_adapter import Adapter
from devices.selector_switch import SelectorSwitch


class SensorSwitch(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        switch = SelectorSwitch(devices, 'switch', 'click')
        switch.add_level('Off', None)
        switch.add_level('Click', 'single')
        switch.add_level('Double Click', 'double')
        switch.add_level('Triple Click', 'triple')
        switch.add_level('Quadruple Click', 'quadruple')
        switch.add_level('Many clicks', 'many')
        switch.add_level('Long Click', 'long')
        switch.add_level('Long Click Release', 'long_release')
        switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)

        self.devices.append(switch)
