from devices.boolean_sensor import BooleanSensor


class ContactSensor(BooleanSensor):
    def __init__(self, devices, alias, value_key, device_name_suffix = ''):
        super().__init__(devices, alias, value_key, BooleanSensor.SENSOR_TYPE_CONTACT, device_name_suffix)
