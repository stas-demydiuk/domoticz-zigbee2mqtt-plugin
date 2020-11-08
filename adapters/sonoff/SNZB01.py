from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class SNZB01(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Click', 'single')
        self.switch.add_level('Double Click', 'double')
        self.switch.add_level('Long Press', 'long')

        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.switch.disable_value_check_on_update()

        self.devices.append(self.switch)

    def handle_command(self, alias, device, command, level, color):
        device_data = self._get_legacy_device_data()
        self.switch.handle_command(device_data, command, level, color)
