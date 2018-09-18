from adapters.boolean_sensor import BooleanSensor

class SensorMotion(BooleanSensor):
    def __init__(self, devices):
        super().__init__(devices)
        self.sensor_type = self.SENSOR_TYPE_MOTION
        self.senor_value_key = 'occupancy'