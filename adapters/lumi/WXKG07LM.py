from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class WXKG07LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switchLeft = SelectorSwitch(devices, 'switch' + str(0), 'action', ' (Left Click)')
        self.switchLeft.add_level("Off", None)
        self.switchLeft.add_level('Click', 'left')
        self.switchLeft.add_level('Long click', 'left_long')
        self.switchLeft.add_level('Double click', 'left_double')
        self.switchLeft.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.switchLeft.disable_value_check_on_update()
        self.switchRight = SelectorSwitch(devices, 'switch' + str(1), 'click', ' (Right Button)')
        self.switchRight.add_level('Click', 'right')
        self.switchRight.add_level('Long click', 'right_long')
        self.switchRight.add_level('Double click', 'right_double')
        self.switchRight.disable_value_check_on_update()
        self.switchBoth = SelectorSwitch(devices, 'switch' + str(2), 'click', ' ( Both Buttons)')
        self.switchBoth.add_level('Click', 'both')
        self.switchBoth.add_level('Long Click', 'both_long')
        self.switchBoth.add_level('Double Click', 'both_double')
        self.switchBoth.disable_value_check_on_update()

        self.devices.append(self.switchLeft)
        self.devices.append(self.switchRight)
        self.devices.append(self.switchBoth)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'click' in message.raw:
            message.raw['state'] = message.raw['click']
        elif 'action' in message.raw:
            message.raw['state'] = message.raw['action']

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switchLeft.handle_command(device_data, command, level, color)
        self.switchRight.handle_command(device_data, command, level, color)
        self.switchBoth.handle_command(device_data, command, level, color)
