import Domoticz
from adapters.base_adapter import Adapter
from devices.switch.push_on_button import PushOnButton


class WXKG03LM(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(PushOnButton(devices, 'switch', 'state'))

    def convert_message(self, message):
        if 'click' in message.raw:
            message.raw['state'] = 'on' if message['click'] == 'single' else 'off'

        return message
