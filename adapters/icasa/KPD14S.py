from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch
from devices.switch.dimmer_switch import DimmerSwitch


class KPD14S(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        button = SelectorSwitch(devices, 'click', 'click', ' (State)')
        button.add_level('Off', 'off')
        button.add_level('On', 'on')
        button.add_level('S1', 1)
        button.add_level('S2', 2)
        button.disable_value_check_on_update()

        self.devices.append(button)
        self.devices.append(DimmerSwitch(devices, 'light', 'brightness', ' (Brightness)'))

    def handle_command(self, alias, device, command, level, color):
        device_data = self._get_legacy_device_data()
        device = self.get_device_by_alias(alias)

        if device != None:
            device.handle_command(device_data, command, level, color)
