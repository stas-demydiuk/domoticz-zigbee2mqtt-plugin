from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class ZYCT202(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        buttons_count = 6

        for btn_index in range(1, buttons_count + 1):
            self.devices.append(self.create_button(devices, btn_index))

    def create_button(self, devices, index):
        button = SelectorSwitch(devices, 'btn' + str(index), 'action', ' (Button ' + str(index) + ')')
        button.add_level('Off', None)
        button.add_level('On', 'on')
        button.add_level('Up', 'up-press')
        button.add_level('Down', 'down-press')
        button.add_level('Stop', 'stop')
        button.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        button.disable_value_check_on_update()

        return button

    def handleCommand(self, alias, device, device_data, command, level, color):
        device = self.get_device_by_alias(alias)
        device.handle_command(device_data, command, level, color)

    def handleMqttMessage(self, device_data, message):
        if 'action' not in message.raw or 'action_group' not in message.raw:
            return

        converted_message = self.convert_message(message)
        btn_index = message.raw['action_group'] - 144

        device = self.get_device_by_alias('btn' + str(btn_index))
        device.handle_message(device_data, converted_message)

        self.update_battery_status(device_data, converted_message)
        self.update_link_quality(device_data, converted_message)
