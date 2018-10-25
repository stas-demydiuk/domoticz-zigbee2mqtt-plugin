from adapters.base_adapter import Adapter
from devices.selector_switch import SelectorSwitch


class WXKG02LM(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'click')
        self.switch.add_level('Off', None)
        self.switch.add_level('Switch 1', 'left')
        self.switch.add_level('Switch 2', 'right')
        self.switch.add_level('Both_Click', 'both')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)

        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
