import Domoticz
import json
from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.temperature import TemperatureSensor
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.level_switch import LevelSwitch
from devices.switch.selector_switch import SelectorSwitch
from devices.setpoint import SetPoint



class TS0601(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        mode_switch = SelectorSwitch(devices, 'mode', 'system_mode', ' (Mode)')
        mode_switch.add_level('Off', 'off')
        mode_switch.add_level('Auto', 'auto')
        mode_switch.add_level('Manual', 'manual')
        mode_switch.add_level('Comfort', 'comfort')
        mode_switch.add_level('Eco', 'eco')
        mode_switch.add_level('Boost', 'boost')
        mode_switch.add_level('Complex', 'complex')
        mode_switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        mode_switch.set_icon(15)

        preset = SelectorSwitch(devices, 'preset', 'preset', ' (Preset)')
        preset.add_level('Away', 'away')
        preset.add_level('Schedule', 'schedule')
        preset.add_level('Manual', 'manual')
        preset.add_level('Comfort', 'comfort')
        preset.add_level('Eco', 'eco')
        preset.add_level('Boost', 'boost')
        preset.add_level('Complex', 'complex')
        preset.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        preset.set_icon(15)

        week_format = SelectorSwitch(devices, 'week', 'week', ' (Week Format)')
        week_format.add_level('5+2', '5+2')
        week_format.add_level('6+1', '6+1')
        week_format.add_level('7', '7')

        self.devices.append(mode_switch)
        self.devices.append(preset)
        self.devices.append(week_format)
        self.devices.append(SetPoint(devices, 'spoint', 'current_heating_setpoint',' (Setpoint)'))
        self.devices.append(SetPoint(devices, 'sp_eco', 'eco_temperature',' (Eco Setpoint)'))
        self.devices.append(SetPoint(devices, 'sp_cmf', 'comfort_temperature',' (Comfort Setpoint)'))
        self.devices.append(TemperatureSensor(devices, 'temp', 'local_temperature',' (Temperature)'))
        self.devices.append(LevelSwitch(devices, 'level', 'position', ' (Valve position)'))
        self.devices.append(OnOffSwitch(devices, 'wnd', 'window_detection', ' (Window Detection)'))
        self.devices.append(OnOffSwitch(devices, 'child', 'child_lock', ' (Child Lock)'))

    def convert_message(self, message):
        message = super().convert_message(message)
	
        if 'child_lock' in message.raw:
            state = message.raw['child_lock']
            message.raw['child_lock'] = 'ON' if state == 'LOCKED' else 'OFF'

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        topic = device_data['friendly_name'] + '/set'

        if (alias == 'spoint' or alias == 'sp_eco' or alias == 'sp_cmf') and command == 'Set Level':
            switch = self.get_device_by_alias(alias)
            key = switch.value_key

            return {
                'topic': topic,
                'payload': json.dumps({ key: level })
            }

        if alias == 'mode' or alias == 'preset':
            switch = self.get_device_by_alias(alias)
            level_index = int(level / 10)
            msg = json.dumps({ alias: switch.level_values[level_index] })

            return {
                'topic': topic,
                'payload': msg
            }

        if alias == 'week':
            Domoticz.Log('zigbee2mqtt does not support week update')

        if alias == 'wnd':
            return {
                'topic': topic,
                'payload': json.dumps({
                    'window_detection': command.upper()
                })
            }

        if alias == 'child':
            return {
                'topic': topic,
                'payload': json.dumps({
                    'child_lock': 'LOCK' if command.upper() == 'ON' else 'UNLOCK'
                })
            }

        if alias == 'level':
            Domoticz.Log('zigbee2mqtt does not support valve position update')