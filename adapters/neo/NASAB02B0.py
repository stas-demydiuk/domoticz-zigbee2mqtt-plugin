import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch
from devices.sensor.temperature import TemperatureSensor
from devices.sensor.humidity import HumiditySensor
from devices.switch.selector_switch import SelectorSwitch


class NASAB02B0(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', 'temperature'))
        self.devices.append(HumiditySensor(devices, 'hum', 'humidity', ' (Humidity)'))
        self.devices.append(OnOffSwitch(devices, 'alarm', 'alarm', ' (Alarm)'))

        volume_switch = SelectorSwitch(devices, 'vol', 'volume', ' (Volume)')
        volume_switch.add_level('Low', 'low')
        volume_switch.add_level('Medium', 'medium')
        volume_switch.add_level('High', 'high')

        self.devices.append(volume_switch)

    def convert_message(self, message):
        message = super().convert_message(message)
	
        if 'alarm' in message.raw:
            message.raw['alarm'] = 'on' if message.raw['alarm'] else 'off'

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        if alias == 'alarm':
            switch = self.get_device_by_alias(alias)
            switch.handle_command(device_data, command, level, color)

            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "alarm": True if command.upper() == 'ON' else False
                })
            }

        if alias == 'vol':
            switch = self.get_device_by_alias(alias)
            level_index = int(level / 10)
            level_value = switch.level_values[level_index]

            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "volume": level_value
                })
            }
