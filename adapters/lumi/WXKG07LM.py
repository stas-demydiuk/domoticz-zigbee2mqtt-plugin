from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class WXKG07LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switchLeft = SelectorSwitch(devices, 'switch', 'click')
        self.switchLeft.add_level('Switch 1 click', 'left')
        self.switchLeft.add_level('Switch 1 long click', 'left_long')
        self.switchLeft.add_level('Switch 1 double click', 'left_double')
        self.switchLeft.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.switchLeft.disable_value_check_on_update()
        self.switchRight = SelectorSwitch(devices, 'switch', 'click')
        self.switchRight.add_level('Switch 2 click', 'right')
        self.switchRight.add_level('Switch 2 long click', 'right_long')
        self.switchRight.add_level('Switch 2 double click', 'right_double')
        self.switchBoth = SelectorSwitch(devices, 'switch', 'click')
        self.switchBoth.add_level('Both Click', 'both')

        self.devices.append(self.switchLeft)
        self.devices.append(self.switchRight)
        self.devices.append(self.switchBoth)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switchLeft.handle_command(device_data, command, level, color)
        self.switchRight.handle_command(device_data, command, level, color)
        self.switchBoth.handle_command(device_data, command, level, color)
