import domoticz
from devices.device import Device

class TextSensor(Device):
    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Text")

    def get_numeric_value(self, value, device):
        #Work-around, because a text sensor had no numeric value
        return 0

    def get_string_value(self, value, device):
        return str(value)
