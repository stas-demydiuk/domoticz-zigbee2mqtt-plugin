import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch


class GDKES02TZXD(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.devices.append(OnOffSwitch(devices, 'left', 'state_left'))
        self.devices.append(OnOffSwitch(devices, 'right', 'state_right'))

    def handleCommand(self, alias, device, device_data, command, level, color):
        return {
            'topic': '/'.join([device_data['friendly_name'], alias, 'set']),
            'payload': json.dumps({
                "state": command.upper()
            })
        }

