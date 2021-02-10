from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter


konke_adapters = {
    '2AJZ4KPFT': TemperatureHumiditySensorAdapter,  # Konke Temperature and humidity sensor
	'2AJZ4KPBS': MotionSensorAdapter,				# Konke Motion sensor
    'LH07321': WaterLeakSensorAdapter               # Konke Water detector
}