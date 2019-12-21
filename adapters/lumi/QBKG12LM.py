import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.selector_switch import SelectorSwitch
from devices.sensor.kwh import KwhSensor

class QBKG12LM(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        
        selector = SelectorSwitch(devices, 'click', 'click')
        selector.add_level('Off', None)
        selector.add_level('Left', 'left_single')
        selector.add_level('Right', 'right_single')
        selector.add_level('Both', 'both_single')
        selector.disable_value_check_on_update()

        self.devices.append(OnOffSwitch(devices, 'left', 'state_left'))
        self.devices.append(OnOffSwitch(devices, 'right', 'state_right'))
        self.devices.append(selector)
        self.devices.append(KwhSensor(devices, 'kwh', ['power']))

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