import json
from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.selector_switch import SelectorSwitch
from devices.text_sensor import TextSensor


class NimlyLock(AdapterWithBattery):
    def __init__(self):
        super().__init__()
        
        self.lock = OnOffSwitch('lock', 'state', ' (Lock/Unlock)')
        self.auto_relock = OnOffSwitch('auto_relock', 'auto_relock', ' (Auto Relock)')
        self.auto_relock.set_icon(9)
        
        self.unlock_user = TextSensor('last_unlock_user', 'last_unlock_user', ' (Last Unlock User)')
        self.lock_user = TextSensor('last_lock_user', 'last_lock_user', ' (Last Lock User)')
        self.pincode = TextSensor('last_used_pin_code', 'last_used_pin_code', ' (Last Used Pin Code)')
        
        self.lock_state = SelectorSwitch('lock_state', 'lock_state', ' (Lock State)')
        self.lock_state.add_level('Off', None)
        self.lock_state.add_level('Unlocked', 'unlocked')
        self.lock_state.add_level('Locked', 'locked')
        self.lock_state.add_level('Not Fully Locked', 'not_fully_locked')
        self.lock_state.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.lock_state.set_icon(9)
        self.lock_state.disable_value_check_on_update()
                
        self.sound_volume = SelectorSwitch('sound_volume', 'sound_volume', ' (Sound Volume)')
        self.sound_volume.add_level('Off', None)
        self.sound_volume.add_level('Silent', 'silent_mode')
        self.sound_volume.add_level('Low', 'low_volume')
        self.sound_volume.add_level('High', 'high_volume')
        self.sound_volume.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.sound_volume.set_icon(8)
        self.sound_volume.disable_value_check_on_update()
        
        self.unlock_source = SelectorSwitch('last_unlock_source', 'last_unlock_source', ' (Last Unlock Source)')
        self.unlock_source.add_level('Off', None)
        self.unlock_source.add_level('Zigbee', 'zigbee')
        self.unlock_source.add_level('Keypad', 'keypad')
        self.unlock_source.add_level('Fingerprint', 'fingerprintsensor')
        self.unlock_source.add_level('Button', 'self')
        self.unlock_source.add_level('Unknown', 'unknown')
        self.unlock_source.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.unlock_source.set_icon(9)
        self.unlock_source.disable_value_check_on_update()
        
        self.lock_source = SelectorSwitch('last_lock_source', 'last_lock_source', ' (Last Lock Source)')
        self.lock_source.add_level('Off', None)
        self.lock_source.add_level('Zigbee', 'zigbee')
        self.lock_source.add_level('Keypad', 'keypad')
        self.lock_source.add_level('Fingerprint', 'fingerprintsensor')
        self.lock_source.add_level('Button', 'self')
        self.lock_source.add_level('Unknown', 'unknown')
        self.lock_source.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.lock_source.set_icon(9)
        self.lock_source.disable_value_check_on_update()
        
        self.devices.append(self.lock)
        self.devices.append(self.auto_relock)
        
        self.devices.append(self.unlock_user)
        self.devices.append(self.lock_user)
        self.devices.append(self.pincode)
        
        self.devices.append(self.lock_state)
        self.devices.append(self.sound_volume)
        self.devices.append(self.unlock_source)
        self.devices.append(self.lock_source)

    def convert_message(self, message):
        message = super().convert_message(message)
	
        if 'state' in message.raw:
            state = message.raw['state']
            message.raw['state'] = 'ON' if state == 'LOCK' else 'OFF'
            
        if 'auto_relock' in message.raw:
            state = message.raw['auto_relock']
            message.raw['auto_relock'] = 'On' if state == True else 'Off'

        return message

    def handle_command(self, alias, device, command, level, color):
        topic = self.name + '/set'

        if alias == 'lock':
            return {
                'topic': topic,
                'payload': json.dumps({
                    "state": 'LOCK' if command.upper() == 'ON' else 'UNLOCK'
                })
            }
            
        if alias == 'auto_relock':
            return {
                'topic': topic,
                'payload': json.dumps({
                    "auto_relock": True if command.upper() == 'ON' else False
                })
            }
            
        if alias == 'sound_volume':
            switch = self.get_device_by_alias(alias)
            level_index = int(level / 10)
            msg = json.dumps({ alias: switch.level_values[level_index] })

            return {
                'topic': topic,
                'payload': msg
            }


