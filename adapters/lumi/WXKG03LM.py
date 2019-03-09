from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.push_on_button import PushOnButton


class WXKG03LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = PushOnButton(devices, 'switch', 'state')
        self.devices.append(self.switch)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'click' in message.raw:
            message.raw['state'] = 'on' if message.raw['click'] == 'single' else 'off'

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)