import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.selector_switch import SelectorSwitch

class QBKG03LM(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        
        selector = SelectorSwitch(devices, 'click', 'click')
        selector.add_level('Off', None)
        selector.add_level('Left', 'left')
        selector.add_level('Left Double Click', 'left_double')
        selector.add_level('Right', 'right')
        selector.add_level('Right Double Click', 'right_double')
        selector.add_level('Both', 'both')
        selector.disable_value_check_on_update()

        self.devices.append(OnOffSwitch(devices, 'left', 'state_left'))
        self.devices.append(OnOffSwitch(devices, 'right', 'state_right'))
        self.devices.append(selector)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'click' in message.raw:
            message.raw['click'] = message.raw['click'].replace('_single', '')

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        if alias == 'left' or alias == 'right':
            return {
                'topic': '/'.join([device_data['friendly_name'], alias, 'set']),
                'payload': json.dumps({
                    "state": command.upper()
                })
            }
        else:
            device = self.get_device_by_alias(alias)

            if device != None:
                device.handle_command(device_data, command, level, color)