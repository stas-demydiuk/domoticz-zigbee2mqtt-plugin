from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class WXKG03LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'state')
        self.switch.add_level('Off', None)
        self.switch.add_level('Click', 'single')
        self.switch.add_level('Double Click', 'double')
        self.switch.add_level('Hold', 'hold')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.switch.disable_value_check_on_update()

        self.devices.append(self.switch)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'click' in message.raw:
            message.raw['state'] = message.raw['click']
        elif 'action' in message.raw:
            message.raw['state'] = message.raw['action']

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
