import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch


class TS0015(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.devices.append(OnOffSwitch(devices, 'l1', 'state_l1'))
        self.devices.append(OnOffSwitch(devices, 'l2', 'state_l2'))
        self.devices.append(OnOffSwitch(devices, 'l3', 'state_l3'))
        self.devices.append(OnOffSwitch(devices, 'l4', 'state_l4'))
        self.devices.append(OnOffSwitch(devices, 'l5', 'state_l5'))

    def handle_command(self, alias, device, command, level, color):
        return {
            'topic': '/'.join([self.name, alias, 'set']),
            'payload': json.dumps({
                "state": command.upper()
            })
        }
