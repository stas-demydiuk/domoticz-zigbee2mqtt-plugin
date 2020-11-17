from adapters.base_adapter import Adapter
from devices.switch.selector_switch import SelectorSwitch


class Immax07046L(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        switch = SelectorSwitch(devices, 'btn', 'action')
        switch.add_level('Off', None)
        switch.add_level('Arm Away', 'arm_away')
        switch.add_level('Arm Stay', 'arm_stay')
        switch.add_level('Disarm', 'disarm')
        switch.add_level('Panic', 'panic')
        self.devices.append(switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        device = self.get_device_by_alias(alias)

        if device != None:
            device.handle_command(device_data, command, level, color)
