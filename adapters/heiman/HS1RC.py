from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch

class HeimanAlarmRemoteAdapter(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'Remote', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Arm all zones', 'arm_all_zones')
        self.switch.add_level('Arm partial zones', 'arm_partial_zones')
        self.switch.add_level('Disarm', 'disarm')
        self.switch.add_level('Emergency', 'emergency')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.devices.append(self.switch)

    def convert_message(self, message):
        message = super().convert_message(message)
        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)


