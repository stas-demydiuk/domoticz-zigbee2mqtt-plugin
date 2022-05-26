import domoticz
from devices.device import Device


class CO2Sensor(Device):
    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, Type=249, Subtype=1, Switchtype=0)

    def get_numeric_value(self, value, device):
        return int(value)

    def get_string_value(self, value, device):
        return '0'
