from devices.boolean_sensor import BooleanSensor

class ContactSensor(BooleanSensor):
    def __init__(self, devices, alias, value_key):
        super().__init__(devices, alias, value_key, BooleanSensor.SENSOR_TYPE_CONTACT)
