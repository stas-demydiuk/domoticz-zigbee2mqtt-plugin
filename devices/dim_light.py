import Domoticz
from devices.device import Device

class DimLight(Device):
    """device class for a dimmable light"""
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=244, Subtype=73, Switchtype=7).Create()

    def get_numeric_value(self, value, device):
        return 1 if value > 0 else 0

    def get_string_value(self, value, device):
        return str(int(value * 100 / 255))

    def get_sn_values(self, key, value, device):
        s_value = None
        n_value = None
        if key == "state" and value.upper() == 'OFF':
            n_value = 0
            s_value = value
        elif key == "brightness":
            n_value = 1 if value > 0 else 0
            s_value = str(int(value * 100 / 255))
        
        return (s_value,n_value)
