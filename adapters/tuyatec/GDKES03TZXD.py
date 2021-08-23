import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch


class GDKES03TZXD(Adapter):
    def __init__(self):
        super().__init__()

        self.devices.append(OnOffSwitch('left', 'state_left'))
        self.devices.append(OnOffSwitch('center', 'state_center'))
        self.devices.append(OnOffSwitch('right', 'state_right'))

    def handle_command(self, alias, device, command, level, color):
        return {
            'topic': '/'.join([self.name, alias, 'set']),
            'payload': json.dumps({
                "state": command.upper()
            })
        }
