from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.push_on_button import PushOnButton


class WXKG03LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(PushOnButton(devices, 'switch', 'state'))

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'click' in message.raw:
            message.raw['state'] = 'on' if message['click'] == 'single' else 'off'

        return message
