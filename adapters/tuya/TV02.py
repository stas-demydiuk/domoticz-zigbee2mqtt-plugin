import domoticz
import json
from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.temperature import TemperatureSensor
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.level_switch import LevelSwitch
from devices.switch.selector_switch import SelectorSwitch
from devices.setpoint import SetPoint


class TV02(AdapterWithBattery):
    def __init__(self):
        super().__init__()

        preset = SelectorSwitch('preset', 'preset', ' (Preset)')
        preset.add_level('Auto', 'auto')
        preset.add_level('Manual', 'manual')
        preset.add_level('Holiday', 'holiday')
        preset.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        preset.set_icon(15)

        self.devices.append(preset)
        self.devices.append(TemperatureSensor('temp', 'local_temperature',' (Temperature)'))
        self.devices.append(SetPoint('spoint', 'current_heating_setpoint',' (Setpoint)'))
        self.devices.append(SetPoint('temp_cal', 'local_temperature_calibration',' (TempCal)'))
        self.devices.append(OnOffSwitch('hs', 'heating_stop',' (Heating Stop)'))
        self.devices.append(OnOffSwitch('child', 'child_lock',' (Child Lock)'))
        self.devices.append(OnOffSwitch('wnd', 'open_window', ' (Open Window)'))

#        week_format = SelectorSwitch('week', 'week', ' (Week Format)')
#        week_format.add_level('5+2', '5+2')
#        week_format.add_level('6+1', '6+1')
#        week_format.add_level('7', '7')
#        self.devices.append(week_format)

#        self.devices.append(SetPoint('sp_eco', 'eco_temperature',' (Eco Setpoint)'))
#        self.devices.append(SetPoint('sp_cmf', 'comfort_temperature',' (Comfort Setpoint)'))

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'child_lock' in message.raw:
            state = message.raw['child_lock']
            message.raw['child_lock'] = 'ON' if state == 'LOCKED' else 'OFF'

        return message

    def handle_command(self, alias, device, command, level, color):
        topic = self.name + '/set'

        if (alias == 'spoint' or alias == 'temp_cal') and command == 'Set Level':
            switch = self.get_device_by_alias(alias)
            key = switch.value_key

            return {
                'topic': topic,
                'payload': json.dumps({ key: level })
            }

        if alias == 'preset':
            switch = self.get_device_by_alias(alias)
            level_index = int(level / 10)
            msg = json.dumps({ alias: switch.level_values[level_index] })

            return {
                'topic': topic,
                'payload': msg
            }

        if alias == 'wnd':
            domoticz.log('zigbee2mqtt does not support week update')

        if alias == 'wnd':
            return {
                'topic': topic,
                'payload': json.dumps({
                    'open_window': command.upper()
                })
            }

        if alias == 'child':
            return {
                'topic': topic,
                'payload': json.dumps({
                    'child_lock': 'LOCK' if command.upper() == 'ON' else 'UNLOCK'
                })
            }

        if alias == 'hs':
            return {
                'topic': topic,
                'payload': json.dumps({
                    'heating_stop': 'OFF' if command.upper() == 'OFF' else 'ON'
                })
            }

        if alias == 'level':
            domoticz.log('zigbee2mqtt does not support valve position update')
