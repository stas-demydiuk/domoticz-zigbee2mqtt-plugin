from adapters.base_adapter import Adapter
from devices.switch.dimmer_switch import DimmerSwitch
from devices.switch.toggle_switch import ToggleSwitch
from devices.switch.selector_switch import SelectorSwitch


class Symfonisk(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        rotation_switch = SelectorSwitch(devices, 'rotate', 'rotation', ' (Rotation)')
        rotation_switch.add_level('Off', 'rotate_stop')
        rotation_switch.add_level('Left', 'rotate_left')
        rotation_switch.add_level('Right', 'rotate_right')
        rotation_switch.disable_value_check_on_update()

        self.devices.append(DimmerSwitch(devices, 'dimmer', 'brightness', ' (Level)'))
        self.devices.append(ToggleSwitch(devices, 'switch', 'click', ' (Switch)'))
        self.devices.append(rotation_switch)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'action' in message.raw: 
            action = message.raw['action']
            
            if action != 'play_pause':
                message.raw['rotation'] = action
            else:
                message.raw['click'] = 'toggle'

        return message
