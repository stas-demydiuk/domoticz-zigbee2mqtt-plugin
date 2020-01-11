import json
from adapters.base_adapter import Adapter
from devices.switch.blind_percentages_switch import BlindSwitch

class TradfriRollerBlind(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(BlindSwitch(devices, 'dimmer', 'position'))

    def handleCommand(self, alias, device, device_data, command, level, color):
        if (command.upper() == "SET LEVEL"):
            return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "position": int(100-level)
            })
            }
        elif (command.upper() == "ON"):
            return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "state": "close"
            })
            }
        else:
            command="open"
            return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "state": "open"
            })
            }
