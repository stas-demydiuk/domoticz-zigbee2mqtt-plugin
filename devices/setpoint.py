import Domoticz
from devices.device import Device


class SetPoint(Device):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=242, Subtype=1).Create()

    def get_numeric_value(self, value, device):
        return 0

    def get_string_value(self, value, device):
        return str(value)
