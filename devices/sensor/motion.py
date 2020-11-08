from devices.boolean_sensor import BooleanSensor


class MotionSensor(BooleanSensor):
    def __init__(self, devices, alias, value_key, device_name_suffix = ''):
        super().__init__(devices, alias, value_key, BooleanSensor.SENSOR_TYPE_MOTION, device_name_suffix)
