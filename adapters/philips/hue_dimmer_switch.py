from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class HueDimmerSwitch(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'dimmer', 'action')
        self.switch.add_level('off', None)
        self.switch.add_level('down-press', 'down-press')
        self.switch.add_level('down-hold', 'down-hold')
        self.switch.add_level('down-hold-release', 'down-hold-release')
        self.switch.add_level('up-press', 'up-press')
        self.switch.add_level('up-hold', 'up-hold')
        self.switch.add_level('up-hold-release', 'up-hold-release')
        self.switch.add_level('on', 'on')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.devices.append(self.switch)
