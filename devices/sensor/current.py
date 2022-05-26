import domoticz
from devices.device import Device


class CurrentSensor(Device):
    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Current (Single)")

    def get_numeric_value(self, value, device):
        return int(value)

    def get_string_value(self, value, device):
        return str(value)
