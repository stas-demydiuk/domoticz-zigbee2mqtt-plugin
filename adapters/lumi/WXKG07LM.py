from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class WXKG07LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switchLeft = SelectorSwitch(devices, 'btn' + str, 'action', ' (Left Click)')
        self.switchLeft.add_level("Off", None)
        self.switchLeft.add_level('Click L', 'left')
        self.switchLeft.add_level('Long click L', 'left_long')
        self.switchLeft.add_level('Double click L', 'left_double')
        # self.switchLeft.disable_value_check_on_update()
        # self.switchRight = SelectorSwitch(devices, 'btn' + str(1), 'action', ' (Right Button)')
        # self.switchRight.add_level("Off", None)
        self.switchLeft.add_level('Click R', 'right')
        self.switchLeft.add_level('Long click R', 'right_long')
        self.switchLeft.add_level('Double click R', 'right_double')
        # self.switchRight.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        # self.switchRight.disable_value_check_on_update()
        # self.switchBoth = SelectorSwitch(devices, 'btn' + str(2), 'action', ' (Both Buttons)')
        # self.switchBoth.add_level("Off", None)
        self.switchLeft.add_level('Click B', 'both')
        self.switchLeft.add_level('Long Click B', 'both_long')
        self.switchLeft.add_level('Double Click B', 'both_double')
        self.switchLeft.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        # self.switchBoth.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        # self.switchBoth.disable_value_check_on_update()

        self.devices.append(self.switchLeft)
        # self.devices.append(self.switchRight)
        # self.devices.append(self.switchBoth)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'click' in message.raw:
            message.raw['state'] = message.raw['click']
        elif 'action' in message.raw:
            message.raw['state'] = message.raw['action']

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switchLeft.handle_command(device_data, command, level, color)
        # self.switchRight.handle_command(device_data, command, level, color)
        # self.switchBoth.handle_command(device_data, command, level, color)
