import json
from adapters.generic.thermostat import ThermostatAdapter
from devices.switch.on_off_switch import OnOffSwitch


class GS361AH04(ThermostatAdapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.devices.append(OnOffSwitch(devices, 'wnd', 'window_detection', ' (Window Detection)'))
        self.devices.append(OnOffSwitch(devices, 'valve', 'valve_detection', ' (Valve Detection)'))
        self.devices.append(OnOffSwitch(devices, 'child', 'child_lock', ' (Child Lock)'))

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'child_lock' in message.raw:
            message.raw['child_lock'] = 'ON' if message.raw['child_lock'] == 'LOCKED' else 'OFF'

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        topic = device_data['friendly_name'] + '/set'

        if alias == 'wnd':
            return {
                'topic': topic,
                'payload': json.dumps({
                    'window_detection': command.upper()
                })
            }
        
        if alias == 'valve':
            return {
                'topic': topic,
                'payload': json.dumps({
                    'valve_detection': command.upper()
                })
            }

        if alias == 'child':
            return {
                'topic': topic,
                'payload': json.dumps({
                    'child_lock': 'LOCK' if command.upper() == 'ON' else 'UNLOCK'
                })
            }

        return super().handleCommand(alias, device, device_data, command, level, color)