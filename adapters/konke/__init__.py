from adapters.contact_adapter import ContactAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from adapters.konke.button import KonkeButton
from adapters.konke.sensor_temp_hum import KonkeTemperatureHumiditySensor

konke_adapters = {
    '2AJZ4KPKEY': KonkeButton,                      # Konke Multi-function button
    '2AJZ4KPFT': KonkeTemperatureHumiditySensor,    # Konke Temperature and humidity sensor
	'2AJZ4KPBS': MotionSensorAdapter,				# Konke Motion sensor
    '2AJZ4KPDR': ContactAdapter,                    # Konke Contact sensor
    'LH07321': WaterLeakSensorAdapter               # Konke Water detector
}