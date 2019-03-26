import Domoticz
from devices.switch.on_off_switch import OnOffSwitch


class ToggleSwitch(OnOffSwitch):
    def get_numeric_value(self, value, device):
        if (value != 'toggle'):
            return device.nValue
        else:
            return 1 if device.nValue == 0 else 0

    def get_string_value(self, value, device):
        return 'On' if self.get_numeric_value(value, device) == 1 else 'Off'