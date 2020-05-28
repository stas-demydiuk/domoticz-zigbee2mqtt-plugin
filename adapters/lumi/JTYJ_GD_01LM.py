import json
from adapters.generic.smoke_sensor import SmokeSensorAdapter
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.selector_switch import SelectorSwitch
from devices.custom_sensor import CustomSensor


class JTYJ_GD_01LM(SmokeSensorAdapter):
    def __init__(self, devices):
        super().__init__(devices)

        sensitivity_switch = SelectorSwitch(devices, 'sens', 'sensitivity', ' (Sensivity)')
        sensitivity_switch.add_level('Low', 'low')
        sensitivity_switch.add_level('Medium', 'medium')
        sensitivity_switch.add_level('High', 'high')

        self.devices.append(OnOffSwitch(devices, 'test', 'test_state', ' (Test)'))
        self.devices.append(sensitivity_switch)
        self.devices.append(CustomSensor(devices, 'dnsty', 'smoke_density', ' (Smoke Density)'))

    def handleCommand(self, alias, device, device_data, command, level, color):
        if alias == 'test':
            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    'selftest': ''
                })
            }

        if alias == 'sens':
            device = self.get_device_by_alias(alias)
            device.handle_command(device_data, command, level, color)

            level_index = int(level / 10)
            value = device.level_values[level_index]

            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    'sensitivity': value
                })
            }
