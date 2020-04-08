from adapters.contact_adapter import ContactAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from adapters.konke.button import KonkeButton


konke_adapters = {
    '2AJZ4KPKEY': KonkeButton,                      # Konke Multi-function button
    '2AJZ4KPFT': TemperatureHumiditySensorAdapter,  # Konke Temperature and humidity sensor
	'2AJZ4KPBS': MotionSensorAdapter,				# Konke Motion sensor
    '2AJZ4KPDR': ContactAdapter,                    # Konke Contact sensor
    'LH07321': WaterLeakSensorAdapter               # Konke Water detector
}