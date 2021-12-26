import domoticz
from devices.device import Device


class VoltageSensor(Device):
    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Voltage")

    def get_voltage_value(self, value):
        if hasattr(self, 'feature'):
            unit = self.feature['unit']

            if (unit == 'mV'):
                return value / 1000
            else:
                return value
        else:
            return value

    def get_numeric_value(self, value, device):
        return int(self.get_voltage_value(value))

    def get_string_value(self, value, device):
        return str(self.get_voltage_value(value))
