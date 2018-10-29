from devices.boolean_sensor import BooleanSensor

class DoorContactSensor(BooleanSensor):
    def __init__(self, devices, alias, value_key):
        super().__init__(devices, alias, value_key, BooleanSensor.SENSOR_TYPE_DOOR_CONTACT)
    
    def get_numeric_value(self, value, device):
        return 0 if value else 1
        
    def get_sn_values(self, key, value, device):
        return (self.get_string_value(value, device),self.get_numeric_value(value, device))
