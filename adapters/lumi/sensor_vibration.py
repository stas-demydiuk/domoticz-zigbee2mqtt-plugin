from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class SensorVibration(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'action', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Vibration', 'vibration')
        self.switch.add_level('Drop', 'drop')
        self.switch.add_level('Tilt', 'tilt')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)

        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
