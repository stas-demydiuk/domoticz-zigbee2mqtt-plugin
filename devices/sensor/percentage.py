import Domoticz
from devices.device import Device


class PercentageSensor(Device):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Percentage").Create()

    def get_numeric_value(self, value, device):
        return int(float(value))

    def get_string_value(self, value, device):
        return str(self.get_numeric_value(value, device))
