import Domoticz
from devices.device import Device


class OnOffSwitch(Device):
    def create_device(self, unit, device_id, device_name, message):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Switch", Image=1).Create()

    def get_numeric_value(self, value, device):
        return 1 if value.lower() == 'on' else 0

    def get_string_value(self, value, device):
        return 'On' if value.lower() == 'on' else 'Off'
        
    def get_sn_values(self, key, value, device):
        return (self.get_string_value(value, device),self.get_numeric_value(value, device))
