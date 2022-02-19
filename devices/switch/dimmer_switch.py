import domoticz
from devices.device import Device


class DimmerSwitch(Device):
    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, Type=244, Subtype=73, Switchtype=7)

    def get_numeric_value(self, value, device):
        return 1 if value > 0 else 0

    def get_string_value(self, value, device):
        return str(int(value * 100 / 255))
        