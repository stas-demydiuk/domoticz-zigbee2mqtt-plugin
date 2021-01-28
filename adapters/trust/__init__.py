from adapters.contact_adapter import ContactAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from adapters.trust.zyct202 import ZYCT202

trust_adapters = {
    'ZPIR-8000': MotionSensorAdapter,   # Trust Motion Sensor
    'ZCTS-808': ContactAdapter,         # Trust Wireless contact sensor
    'ZWLD-100': WaterLeakSensorAdapter, # Trust Water leakage detector
    'ZYCT-202': ZYCT202,                # Trust Remote control
}