import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch


class TS0002(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.devices.append(OnOffSwitch(devices, 'l1', 'state_l1'))
        self.devices.append(OnOffSwitch(devices, 'l2', 'state_l2'))

    def handleCommand(self, alias, device, device_data, command, level, color):
        return {
            'topic': '/'.join([device_data['friendly_name'], alias, 'set']),
            'payload': json.dumps({
                "state": command.upper()
            })
        }
