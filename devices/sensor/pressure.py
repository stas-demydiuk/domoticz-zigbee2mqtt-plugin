import domoticz
from devices.device import Device


class PressureSensor(Device):
    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Pressure")

    def get_numeric_value(self, value, device):
        return 0

    def get_string_value(self, value, device):
        return str(value)
