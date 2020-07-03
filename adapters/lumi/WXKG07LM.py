from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class WXKG07LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switchLeft = SelectorSwitch(devices, 'switch_left', 'click')
        self.switchLeft.add_level('Switch 1', 'left')
        self.switchLeft.add_level('Switch 1', 'left_long')
        self.switchLeft.add_level('Switch 1', 'left_double')
        self.switchLeft.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.switchLeft.disable_value_check_on_update()
        self.switchRight = SelectorSwitch(devices, 'switch_right', 'click')
        self.switchRight.add_level('Switch 2', 'right')
        self.switchRight.add_level('Switch 2', 'right_long')
        self.switchRight.add_level('Switch 2', 'right_double')
        self.switchBoth = SelectorSwitch(devices, 'both_click', 'click')
        self.switchBoth.add_level('Both Click', 'both')

        self.devices.append(self.switchLeft)
        self.devices.append(self.switchRight)
        self.devices.append(self.switchBoth)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switchLeft.handle_command(device_data, command, level, color)
        self.switchRight.handle_command(device_data, command, level, color)
        self.switchBoth.handle_command(device_data, command, level, color)
