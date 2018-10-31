import json
from adapters.base_adapter import Adapter
from devices.switch.dimmer_switch import DimmerSwitch

class NL08_0800(Adapter):
    """adapter for the Nanoleaf Smart Ivy bulbs"""
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(DimmerSwitch(devices, 'light', 'value'))

    def convert_message(self, message):
        if 'state' in message.raw and message.raw['state'].upper() == 'OFF':
            message.raw['value'] = 0
        elif 'brightness' in message.raw:
            message.raw['value'] = message.raw['brightness']

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        if command.upper() == 'ON' or command.upper() == 'OFF':
            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "state": command
                })
            }
        if command.upper() == 'SET LEVEL':
            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "brightness": int(level*255/100)
                })
            }
