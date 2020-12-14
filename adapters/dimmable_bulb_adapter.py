import json
from adapters.base_adapter import Adapter
from devices.switch.dimmer_switch import DimmerSwitch


class DimmableBulbAdapter(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(DimmerSwitch(devices, 'light', 'value'))

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'state' in message.raw and message.raw['state'].upper() == 'OFF':
            message.raw['value'] = 0
        elif 'brightness' in message.raw:
            message.raw['value'] = message.raw['brightness']

        return message

    def handle_command(self, alias, device, command, level, color):
        cmd = command.upper()

        if cmd == 'ON' or cmd == 'OFF':
            return {
                'topic': self.name + '/set',
                'payload': json.dumps({
                    "state": cmd
                })
            }

        if cmd == 'SET LEVEL':
            return {
                'topic': self.name + '/set',
                'payload': json.dumps({
                    "state": "ON",
                    "brightness": int(level * 255 / 100)
                })
            }
