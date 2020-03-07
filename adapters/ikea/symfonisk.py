from adapters.base_adapter import Adapter
from devices.switch.dimmer_switch import DimmerSwitch
from devices.switch.toggle_switch import ToggleSwitch
from devices.switch.selector_switch import SelectorSwitch


class Symfonisk(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.click_actions = ['play_pause','skip_forward','skip_backward']

        rotation_switch = SelectorSwitch(devices, 'rotate', 'rotation', ' (Rotation)')
        rotation_switch.add_level('Left', 'rotate_left')
        rotation_switch.add_level('Off', 'rotate_stop')
        rotation_switch.add_level('Right', 'rotate_right')
        rotation_switch.disable_value_check_on_update()
        rotation_switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)

        control_switch = SelectorSwitch(devices, 'switch', 'click', ' (Switch)')
        control_switch.add_level('Backward', 'skip_forward')
        control_switch.add_level('PlayPause', 'play_pause')
        control_switch.add_level('Forward', 'skip_backward')
        control_switch.disable_value_check_on_update()
        control_switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)

        self.devices.append(DimmerSwitch(devices, 'dimmer', 'brightness', ' (Level)'))
        self.devices.append(rotation_switch)
        self.devices.append(control_switch)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'action' in message.raw: 
            action = message.raw['action']
            
            if action in self.click_actions:
                message.raw['click'] = action
            else:
                message.raw['rotation'] = action

        return message
