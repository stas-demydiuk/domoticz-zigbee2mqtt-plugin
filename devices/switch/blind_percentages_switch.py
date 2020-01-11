import Domoticz
from devices.device import Device


class BlindSwitch(Device):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=244, Subtype=73, Switchtype=13).Create()

    def get_numeric_value(self, value, device):
        if (value==100):
            return 0
        elif (value==0):
            return 1
        else:
            return 2

    def get_string_value(self, value, device):
        return str(int(100-value))
        
