from adapters.base_adapter import Adapter
from devices.selector_switch import SelectorSwitch


class SensorCube(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'cube', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Flip 90', 'flip90')
        self.switch.add_level('Flip 180', 'flip180')
        self.switch.add_level('Tap', 'tap')
        self.switch.add_level('Shake', 'shake')
        self.switch.add_level('Fall', 'fall')
        self.switch.add_level('Slide', 'slide')
        self.switch.add_level('Rotate Left', 'rotate_left')
        self.switch.add_level('Rotate Right', 'rotate_right')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)

        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
