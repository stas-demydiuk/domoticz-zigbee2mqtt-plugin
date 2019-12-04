import json
from adapters.base_adapter import Adapter
from devices.switch.selector_switch import SelectorSwitch


class TradfriRollerBlind(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'click')
        self.switch.add_level('Up', 'open')
        self.switch.add_level('Down', 'close')

        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)

        if (command.upper() == "ON"):
            command="close"
        else:
            command="open"

        return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "state": command.upper()
            })
        }
