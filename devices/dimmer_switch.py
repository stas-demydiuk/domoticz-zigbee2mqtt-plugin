import Domoticz
from devices.device import Device


class DimmerSwitch(Device):
    def create_device(self, unit, device_name, options, message):
        return Domoticz.Device(Name=device_name, Unit=unit, Type=244, Subtype=73, Switchtype=7, Options=options).Create()

    def get_numeric_value(self, value, device):
        return 1 if value > 0 else 0

    def get_string_value(self, value, device):
        return str(int(value * 100 / 255))
