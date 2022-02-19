from devices.boolean_sensor import BooleanSensor


class SmokeSensor(BooleanSensor):
    def __init__(self, alias, value_key, device_name_suffix = ''):
        super().__init__(alias, value_key, BooleanSensor.SENSOR_TYPE_SMOKE, device_name_suffix)
