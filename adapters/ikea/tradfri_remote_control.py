from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch
from devices.switch.toggle_switch import ToggleSwitch


class TradfriRemoteControl(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = ToggleSwitch(devices, 'switch', 'action')

        self.arrow_left = SelectorSwitch(devices, 'arrowL', 'action', ' (Left Arrow)')
        self.arrow_left.add_level('Off', None)
        self.arrow_left.add_level('Click', 'arrow_left_click')
        self.arrow_left.add_level('Hold', 'arrow_left_hold')
        self.arrow_left.add_level('Release', 'arrow_left_release')
        self.arrow_left.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.arrow_left.disable_value_check_on_update()

        self.arrow_right = SelectorSwitch(devices, 'arrowR', 'action', ' (Right Arrow)')
        self.arrow_right.add_level('Off', None)
        self.arrow_right.add_level('Click', 'arrow_right_click')
        self.arrow_right.add_level('Hold', 'arrow_right_hold')
        self.arrow_right.add_level('Release', 'arrow_right_release')
        self.arrow_right.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.arrow_right.disable_value_check_on_update()

        self.brightness_up = SelectorSwitch(devices, 'brUp', 'action', ' (Brightness Up)')
        self.brightness_up.add_level('Off', None)
        self.brightness_up.add_level('Click', 'brightness_up_click')
        self.brightness_up.add_level('Hold', 'brightness_up_hold')
        self.brightness_up.add_level('Release', 'brightness_up_release')
        self.brightness_up.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.brightness_up.disable_value_check_on_update()

        self.brightness_down = SelectorSwitch(devices, 'brDown', 'action', ' (Brightness Down)')
        self.brightness_down.add_level('Off', None)
        self.brightness_down.add_level('Click', 'brightness_down_click')
        self.brightness_down.add_level('Hold', 'brightness_down_hold')
        self.brightness_down.add_level('Release', 'brightness_down_release')
        self.brightness_down.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.brightness_down.disable_value_check_on_update()

        self.devices.append(self.switch)
        self.devices.append(self.arrow_left)
        self.devices.append(self.arrow_right)
        self.devices.append(self.brightness_up)
        self.devices.append(self.brightness_down)


    def handleCommand(self, alias, device, device_data, command, level, color):
        device = self.get_device_by_alias(alias)

        if device != None:
            device.handle_command(device_data, command, level, color)

    def handleMqttMessage(self, device_data, message):
        if 'action' not in message.raw:
            return

        converted_message = self.convert_message(message)
        action = message.raw['action']
        
        if action == 'toggle':
            self.switch.handle_message(device_data, converted_message)
        
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