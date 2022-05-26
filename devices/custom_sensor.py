import domoticz
from devices.device import Device


class CustomSensor(Device):
    def create_device(self, unit, device_id, device_name):
        options = {}

        if hasattr(self, 'feature') and 'unit' in self.feature:
            options['Custom'] = '1;' + self.feature['unit']

        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Custom", Options=options)

    def get_numeric_value(self, value, device):
        return int(value)

    def get_string_value(self, value, device):
        return str(value)
