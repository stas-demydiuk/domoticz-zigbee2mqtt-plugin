from adapters.base_adapter import Adapter
from devices.switch.selector_switch import SelectorSwitch


class WXKG12LM(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'state')
        self.switch.add_level('Off', None)
        self.switch.add_level('Click', 'single')
        self.switch.add_level('Double Click', 'double')
        self.switch.add_level('Shake', 'shake')
        self.switch.add_level('Hold', 'hold')
        self.switch.add_level('Release', 'release')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)

        self.devices.append(self.switch)

    def convert_message(self, message):
        if 'click' in message.raw:
            message.raw['state'] = message['click']
        elif 'action' in message.raw:
            message.raw['state'] = message['action']

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
