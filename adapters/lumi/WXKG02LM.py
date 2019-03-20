from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class WXKG02LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'click')
        self.switch.add_level('Off', None)
        self.switch.add_level('Switch 1', 'left')
        self.switch.add_level('Switch 2', 'right')
        self.switch.add_level('Both_Click', 'both')
        self.switch.add_level('Switch 1 Double Click', 'left_double')
        self.switch.add_level('Switch 2 Double Click', 'right_double')
        self.switch.add_level('Both Double Click', 'both_double')
        self.switch.add_level('Switch 1 Long Click', 'left_long')
        self.switch.add_level('Switch 2 Long Click', 'right_long')
        self.switch.add_level('Both Long Click', 'both_long')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)

        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
