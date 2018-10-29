import Domoticz
from devices.device import Device

class VoltageSensor(Device):
    def create_device(self, unit, device_id, device_name, message):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Voltage").Create()

    def get_numeric_value(self, value, device):
        return int(value)

    def get_string_value(self, value, device):
        return str(value)

        
    def get_sn_values(self, key, value, device):
        return (self.get_string_value(value, device),self.get_numeric_value(value, device))
    