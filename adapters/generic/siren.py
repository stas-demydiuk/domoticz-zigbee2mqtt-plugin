import json
from adapters.base_adapter import Adapter
from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.on_off_switch import OnOffSwitch

# TODO: Think how to reuse the code between classes
class SirenAdapter(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.switch = OnOffSwitch(devices, 'switch', 'state')
        self.switch.set_icon(13)
        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)

        mode = 'emergency' if command.upper() == 'ON' else 'stop'

        return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                'warning': {
                    'mode': mode,
                    'duration': 10
                }
            })
        }

class SirenAdapterWithBattery(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.switch = OnOffSwitch(devices, 'switch', 'state')
        self.switch.set_icon(13)
        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)

        mode = 'emergency' if command.upper() == 'ON' else 'stop'

        return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                'warning': {
                    'mode': mode,
                    'duration': 10
                }
            })
        }