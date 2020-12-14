import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch


class WeiserLock(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.switch = OnOffSwitch(devices, 'switch', 'state')
        self.devices.append(self.switch)

    def convert_message(self, message):
        message = super().convert_message(message)
	
        if 'state' in message.raw:
            state = message.raw['state']
            message.raw['state'] = 'ON' if state == 'LOCK' else 'OFF'

        return message

    def handle_command(self, alias, device, command, level, color):
        device_data = self._get_legacy_device_data()
        self.switch.handle_command(device_data, command, level, color)

        return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "state": 'LOCK' if command.upper() == 'ON' else 'UNLOCK'
            })
        }
