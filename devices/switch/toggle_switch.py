import Domoticz
from devices.switch.on_off_switch import OnOffSwitch


class ToggleSwitch(OnOffSwitch):
    def get_numeric_value(self, value, device):
        if (value == 'toggle'):
            return 1 if device.nValue == 0 else 0
        else:
            return super().get_numeric_value(value, device)