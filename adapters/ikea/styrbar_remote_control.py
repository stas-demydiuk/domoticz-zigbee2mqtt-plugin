from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class StyrbarRemoteControl(AdapterWithBattery):
    def __init__(self):
        super().__init__()

        self.brightness_up = SelectorSwitch('brUp', 'action', ' (Brightness Up)')
        self.brightness_up.add_level('Off', None)
        self.brightness_up.add_level('Push', 'on')
        self.brightness_up.add_level('Hold', 'brightness_move_up')
        self.brightness_up.add_level('Release', 'brightness_stop')
        self.brightness_up.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.brightness_up.disable_value_check_on_update()

        self.brightness_down = SelectorSwitch('brDown', 'action', ' (Brightness Down)')
        self.brightness_down.add_level('Off', None)
        self.brightness_down.add_level('Push', 'off')
        self.brightness_down.add_level('Hold', 'brightness_move_down')
        self.brightness_down.add_level('Release', 'brightness_stop')
        self.brightness_down.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.brightness_down.disable_value_check_on_update()
        
        self.arrow_left = SelectorSwitch('arrowL', 'action', ' (Left Arrow)')
        self.arrow_left.add_level('Off', None)
        self.arrow_left.add_level('Push', 'arrow_left_click')
        self.arrow_left.add_level('Hold', 'arrow_left_hold')
        self.arrow_left.add_level('Release', 'arrow_left_release')
        self.arrow_left.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.arrow_left.disable_value_check_on_update()

        self.arrow_right = SelectorSwitch('arrowR', 'action', ' (Right Arrow)')
        self.arrow_right.add_level('Off', None)
        self.arrow_right.add_level('Push', 'arrow_right_click')
        self.arrow_right.add_level('Hold', 'arrow_right_hold')
        self.arrow_right.add_level('Release', 'arrow_right_release')
        self.arrow_right.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.arrow_right.disable_value_check_on_update()

        self.devices.append(self.brightness_up)
        self.devices.append(self.brightness_down)
        self.devices.append(self.arrow_left)
        self.devices.append(self.arrow_right)


    def handle_command(self, alias, device, command, level, color):
        device_data = self._get_legacy_device_data()
        device = self.get_device_by_alias(alias)

        if device != None:
            device.handle_command(device_data, command, level, color)

    def handle_mqtt_message(self, message):
        if 'action' not in message.raw:
            return

        device_data = self._get_legacy_device_data()
        converted_message = self.convert_message(message)
        action = message.raw['action']
        
        if action == None:
            return
        
        if action.startswith('brightness_up'):
            self.brightness_up.handle_message(device_data, converted_message)

        if action.startswith('brightness_down'):
            self.brightness_down.handle_message(device_data, converted_message)

        if action.startswith('arrow_right'):
            self.arrow_right.handle_message(device_data, converted_message)

        if action.startswith('arrow_left'):
            self.arrow_left.handle_message(device_data, converted_message)

        self.update_battery_status(device_data, converted_message)
        self.update_link_quality(device_data, converted_message)
