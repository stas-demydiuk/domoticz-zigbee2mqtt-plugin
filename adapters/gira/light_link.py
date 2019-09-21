from adapters.base_adapter import Adapter
from devices.switch.selector_switch import SelectorSwitch


class GiraLightLink(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'action')
        self.switch.add_level('Off', 'off')
        self.switch.add_level('On', 'on')
        self.switch.add_level('1', '1')
        self.switch.add_level('2', '2')
        self.switch.add_level('3', '3')
        self.switch.add_level('4', '4')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.switch.disable_value_check_on_update()

        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
