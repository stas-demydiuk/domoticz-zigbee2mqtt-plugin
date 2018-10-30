from devices.boolean_sensor import BooleanSensor

class DoorContactSensor(BooleanSensor):
    def __init__(self, devices, alias, value_key):
        super().__init__(devices, alias, value_key, BooleanSensor.SENSOR_TYPE_DOOR_CONTACT)
    
    def get_numeric_value(self, value, device):
        return 0 if value else 1
        