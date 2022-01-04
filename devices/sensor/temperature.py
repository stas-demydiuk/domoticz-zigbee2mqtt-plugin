from decimal import Decimal
import domoticz
from devices.device import Device


class TemperatureSensor(Device):
    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Temperature")

    def get_numeric_value(self, value, device):
        return 0

    def get_string_value(self, value, device):
        return str(round(Decimal(value)+Decimal(device.Adjustment), 1))
