from adapters.base_adapter import Adapter
from devices.selector_switch import SelectorSwitch


class SensorCube(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        switch = SelectorSwitch(devices, 'cube', 'action')
        switch.add_level('Off', None)
        switch.add_level('Flip 90', 'flip90')
        switch.add_level('Flip 180', 'flip180')
        switch.add_level('Tap', 'tap')
        switch.add_level('Shake', 'shake')
        switch.add_level('Fall', 'fall')
        switch.add_level('Slide', 'slide')
        switch.add_level('Rotate Left', 'rotate_left')
        switch.add_level('Rotate Right', 'rotate_right')
        switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)

        self.devices.append(switch)
