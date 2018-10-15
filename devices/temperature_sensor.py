import Domoticz
from devices.device import Device

class TemperatureSensor(Device):
    def create_device(self, unit, device_id, device_name, message):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Temperature").Create()

    def get_numeric_value(self, value, device):
        return 0

    def get_string_value(self, value, device):
        return str(value)

    