from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter


sonoff_adapters = {
    'SNZB-02': TemperatureHumiditySensorAdapter,    # SONOFF Temperature and humidity sensor
    'SNZB-03': MotionSensorAdapter,                 # SONOFF Motion sensor
}
