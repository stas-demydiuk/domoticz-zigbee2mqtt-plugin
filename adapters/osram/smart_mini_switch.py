from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class SmartMiniSwitch(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Up', 'up')
        self.switch.add_level('Up: hold', 'up_hold')
        self.switch.add_level('Up: release', 'up_release')
        self.switch.add_level('Circle: click', 'circle_click')
        self.switch.add_level('Circle: hold', 'circle_hold')
        self.switch.add_level('Circle: release', 'circle_release')
        self.switch.add_level('Down', 'down')
        self.switch.add_level('Down: hold', 'down_hold')
        self.switch.add_level('Down: release', 'down_release')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.switch.disable_value_check_on_update()

        self.devices.append(self.switch)

    def handle_command(self, alias, device, command, level, color):
        device_data = self._get_legacy_device_data()
        self.switch.handle_command(device_data, command, level, color)
