
from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class AqaraOppleSwitch(AdapterWithBattery):
    def __init__(self, devices, buttons_count):
        super().__init__(devices)

        self.buttons_count = buttons_count

        for btn_index in range(1, self.buttons_count + 1):
            self.devices.append(self.create_button(devices, btn_index))

    def create_button(self, devices, index):
        action_prefix = 'button_' + str(index) + '_'
        button = SelectorSwitch(devices, 'btn' + str(index), 'action', ' (Button ' + str(index) + ')')
        button.add_level('Off', None)
        button.add_level('Click', action_prefix + 'single')
        button.add_level('Double', action_prefix + 'double')
        button.add_level('Triple', action_prefix + 'triple')
        button.add_level('Hold', action_prefix + 'hold')
        button.add_level('Release', action_prefix + 'release')
        button.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        button.disable_value_check_on_update()

        return button

    def handle_command(self, alias, device, command, level, color):
        device = self.get_device_by_alias(alias)
        device_data = self._get_legacy_device_data()

        if device != None:
            device.handle_command(device_data, command, level, color)

    def handle_mqtt_message(self, message):
        if 'action' not in message.raw:
            return

        device_data = self._get_legacy_device_data()
        converted_message = self.convert_message(message)
        action = message.raw['action']

        for btn_index in range(1, self.buttons_count + 1):
            if action.startswith('button_' + str(btn_index)):
                device = self.get_device_by_alias('btn' + str(btn_index))
                device.handle_message(device_data, converted_message)

        self.update_battery_status(device_data, converted_message)
        self.update_link_quality(device_data, converted_message)
