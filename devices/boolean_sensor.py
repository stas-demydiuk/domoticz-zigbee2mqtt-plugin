import domoticz
from devices.device import Device


class BooleanSensor(Device):
    SENSOR_TYPE_CONTACT = 2
    SENSOR_TYPE_SMOKE = 5
    SENSOR_TYPE_MOTION = 8
    SENSOR_TYPE_DOOR_CONTACT = 11

    def __init__(self, alias, value_key, sensor_type, device_name_suffix = ''):
        super().__init__(alias, value_key, device_name_suffix)
        self.sensor_type = sensor_type
        self.icon = 0

    def set_icon(self, icon_number):
        self.icon = icon_number

    def create_device(self, unit, device_id, device_name):
        if (self.sensor_type == None):
            domoticz.error('Sensor type is not specified')
            return

        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, Type=244, Subtype=73, Switchtype=self.sensor_type, Image=self.icon)

    def get_numeric_value(self, value, device):
        if hasattr(self, 'feature'):
            if 'value_on' in self.feature and value == self.feature['value_on']:
                return 1
            if 'value_off' in self.feature and value == self.feature['value_off']:
                return 0
            else:
                return device.nValue
        else:
            return 1 if value else 0

    def get_string_value(self, value, device):
        return str(self.get_numeric_value(value, device))
