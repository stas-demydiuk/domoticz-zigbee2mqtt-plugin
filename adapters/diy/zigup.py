import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch
from devices.sensor.temperature import TemperatureSensor
from devices.sensor.voltage import VoltageSensor


class ZigupAdapter(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        
        self.devices.append(OnOffSwitch(devices, 'switch', 'state', ' (State)'))
        self.devices.append(TemperatureSensor(devices, 'temp', 'cpu_temperature', ' (CPU Temperature)'))
        self.devices.append(TemperatureSensor(devices, 'temp_e', 'external_temperature', ' (External Temperature)'))
        self.devices.append(VoltageSensor(devices, 'adc', 'adc_volt', ' (ADC Voltage)'))

    def handleCommand(self, alias, device, device_data, command, level, color):
        device = self.get_device_by_alias(alias)
        device.handle_command(device_data, command, level, color)

        if alias == 'switch':
            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "state": command.upper()
                })
            }
