import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch
from devices.sensor.temperature import TemperatureSensor
from devices.sensor.voltage import VoltageSensor


class ZigupAdapter(Adapter):
    def __init__(self):
        super().__init__()
        
        self.devices.append(OnOffSwitch('switch', 'state', ' (State)'))
        self.devices.append(TemperatureSensor('temp', 'cpu_temperature', ' (CPU Temperature)'))
        self.devices.append(TemperatureSensor('temp_e', 'external_temperature', ' (External Temperature)'))
        self.devices.append(VoltageSensor('adc', 'adc_volt', ' (ADC Voltage)'))

    def handle_command(self, alias, device, command, level, color):
        device_data = self._get_legacy_device_data()
        device = self.get_device_by_alias(alias)
        device.handle_command(device_data, command, level, color)

        if alias == 'switch':
            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "state": command.upper()
                })
            }
