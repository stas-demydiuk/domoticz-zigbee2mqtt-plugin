from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class WXKG01LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Click', 'single')
        self.switch.add_level('Double Click', 'double')
        self.switch.add_level('Triple Click', 'triple')
        self.switch.add_level('Quadruple Click', 'quadruple')
        self.switch.add_level('Many clicks', 'many')
        self.switch.add_level('Long Click', 'long')
        self.switch.add_level('Long Click Release', 'long_release')
        self.switch.add_level('Hold', 'hold')
        self.switch.add_level('Release', 'release')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.switch.disable_value_check_on_update()

        self.devices.append(self.switch)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'click' in message.raw:
            message.raw['action'] = message.raw['click']

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
