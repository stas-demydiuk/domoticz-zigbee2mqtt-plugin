from adapters.base_adapter import Adapter
from devices.switch.selector_switch import SelectorSwitch
from devices.sensor.contact import ContactSensor


class SmartLock(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'key', 'inserted')
        self.switch.add_level('Key 1', '01')
        self.switch.add_level('Key 2', '02')
        self.switch.add_level('Key 3', '03')
        self.switch.add_level('Key 4', '04')
        self.switch.add_level('Key 5', '05')
        self.switch.add_level('Strange', 'strange')
        self.switch.add_level('Unknown', 'unknown')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.devices.append(self.switch)

        self.devices.append(ContactSensor(devices, 'error', 'keyerror'))
