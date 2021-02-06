from adapters.contact_adapter import ContactAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter

ewelink_adapters = {
    'RHK06': ContactAdapter,                    # eWeLink Contact sensor
    'RHK08': TemperatureHumiditySensorAdapter,  # eWeLink Temperature and humidity sensor
    'RHK09': MotionSensorAdapter,               # eWeLink Motion sensor
}
