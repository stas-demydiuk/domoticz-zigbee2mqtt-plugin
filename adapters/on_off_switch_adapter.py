import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch


class OnOffSwitchAdapter(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.switch = OnOffSwitch(devices, 'switch', 'state')
        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)

        return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "state": command.upper()
            })
        }
