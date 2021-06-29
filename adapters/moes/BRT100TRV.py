import Domoticz
import json
from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.temperature import TemperatureSensor
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.level_switch import LevelSwitch
from devices.switch.selector_switch import SelectorSwitch
from devices.setpoint import SetPoint


class BRT100TRV(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        preset = SelectorSwitch(devices, 'preset', 'preset', ' (Preset)')
        preset.add_level('Programming', 'programming')
        preset.add_level('Manual', 'manual')
        preset.add_level('Temporary_manual', 'temporary_manual')
        preset.add_level('Holiday', 'holiday')
        preset.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        preset.set_icon(15)

        self.devices.append(preset)
        self.devices.append(TemperatureSensor(devices, 'temp', 'local_temperature',' (Temperature)'))
        self.devices.append(SetPoint(devices, 'spoint', 'current_heating_setpoint',' (Setpoint)'))
        self.devices.append(SetPoint(devices, 'sp_eco', 'eco_temperature',' (Eco Setpoint)'))
        self.devices.append(OnOffSwitch(devices, 'child', 'child_lock', ' (Child Lock)'))
        self.devices.append(OnOffSwitch(devices, 'eco', 'eco_mode', ' (Eco Mode)'))
        
########      Please do not delete is temporarily canceled.

#        self.devices.append(SetPoint(devices, 'sp_min_temp', 'min_temperature',' (Min_Temperature)'))
#        self.devices.append(SetPoint(devices, 'sp_max_temp', 'max_temperature',' (Max_Temp Setpoint)'))
#        self.devices.append(SetPoint(devices, 'temp_cal', 'local_temperature_calibration',' (Temperature_calibration)'))
#        self.devices.append(LevelSwitch(devices, 'level', 'position', ' (Valve position)'))
#        self.devices.append(OnOffSwitch(devices, 'wnd', 'window_detection', ' (Window Detection)'))
        

    def convert_message(self, message):
        message = super().convert_message(message)
	
        if 'child_lock' in message.raw:
            state = message.raw['child_lock']
            message.raw['child_lock'] = 'ON' if state == 'LOCK' else 'OFF'

        return message

    def handle_command(self, alias, device, command, level, color):
        topic = self.name + '/set'

        if (alias == 'spoint' or alias == 'sp_eco' or alias == 'sp_max_temp' or alias == 'sp_min_temp' or alias == 'temp_cal') and command == 'Set Level':
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
            Domoticz.Log('zigbee2mqtt does not support window update')

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
        
        if alias == 'eco':
            return {
                'topic': topic,
                'payload': json.dumps({
                    'eco_mode': 'OFF' if command.upper() == 'OFF' else 'ON'
                })
            }

        if alias == 'level':
            Domoticz.Log('zigbee2mqtt does not support valve position update')