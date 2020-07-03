from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class WXKG07LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switchLeft = SelectorSwitch(devices, 'switch', 'click', ' (Left Click)')
        self.switchLeft.add_level('Click', 'left')
        self.switchLeft.add_level('Long click', 'left_long')
        self.switchLeft.add_level('Double click', 'left_double')
        self.switchLeft.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.switchLeft.disable_value_check_on_update()
        self.switchRight = SelectorSwitch(devices, 'switch', 'click', ' (Right Button)')
        self.switchRight.add_level('Click', 'right')
        self.switchRight.add_level('Long click', 'right_long')
        self.switchRight.add_level('Double click', 'right_double')
        self.switchBoth = SelectorSwitch(devices, 'switch', 'click', ' ( Both Buttons)')
        self.switchBoth.add_level('Click', 'both')
        self.switchBoth.add_level('Long Click', 'both_long')
        self.switchBoth.add_level('Double Click', 'both_double')

        self.devices.append(self.switchLeft)
        self.devices.append(self.switchRight)
        self.devices.append(self.switchBoth)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switchLeft.handle_command(device_data, command, level, color)
        self.switchRight.handle_command(device_data, command, level, color)
        self.switchBoth.handle_command(device_data, command, level, color)
