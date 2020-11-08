from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class TS0041(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'action', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Click', 'single')
        self.switch.add_level('Double Click', 'double')
        self.switch.add_level('Hold', 'hold')
        self.switch.disable_value_check_on_update()

        self.devices.append(self.switch)

    def handle_command(self, alias, device, command, level, color):
        device_data = self._get_legacy_device_data()
        return self.get_device_by_alias(alias).handle_command(device_data, command, level, color)