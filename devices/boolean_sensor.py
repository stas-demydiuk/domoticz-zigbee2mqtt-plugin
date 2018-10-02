import Domoticz
from devices.device import Device

class BooleanSensor(Device):
    SENSOR_TYPE_CONTACT = 2
    SENSOR_TYPE_MOTION = 8
    SENSOR_TYPE_DOOR_CONTACT = 11

    def __init__(self, devices, alias, value_key, sensor_type):
        super().__init__(devices, alias, value_key)
        self.sensor_type = sensor_type
        
    def create_device(self, unit, device_name, options, message):
        if (self.sensor_type == None):
            Domoticz.Error('Sensor type is not specified')
            return

        return Domoticz.Device(Name=device_name, Unit=unit, Type=244, Subtype=73, Switchtype=self.sensor_type, Options=options).Create()

    def get_numeric_value(self, value, device):
        return 1 if value else 0

    def get_string_value(self, value, device):
        return str(self.get_numeric_value(value, device))