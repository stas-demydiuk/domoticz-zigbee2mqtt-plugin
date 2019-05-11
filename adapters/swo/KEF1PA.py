from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch

class KEF1PA(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'KEF1PA', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Panic', 'panic')
        self.switch.add_level('Home', 'home')
        self.switch.add_level('Away', 'away')
        self.switch.add_level('Sleep', 'sleep')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
