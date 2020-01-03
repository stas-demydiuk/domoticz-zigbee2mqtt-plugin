from adapters.contact_adapter import ContactAdapter
from adapters.generic.smoke_sensor import SmokeSensorAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from adapters.heiman.HS1CAE import HS1CAE
from adapters.heiman.HS1WLE import HS1WLE
from adapters.heiman.HS2SK import HS2SK


heiman_adapters = {
    'HS1CA-E': HS1CAE,                  # HEIMAN Monoxyde detector
    'HS1DS': ContactAdapter,            # HEIMAN Door sensor
    'HS1DS-E': ContactAdapter,          # HEIMAN Door sensor
    'HS1SA': SmokeSensorAdapter,        # HEIMAN Smoke detector
    'HS1WL': WaterLeakSensorAdapter,    # HEIMAN Water leakage sensor
    'HS1-WL-E': HS1WLE,                 # HEIMAN Water leakage sensor
    'HS2SK': HS2SK,                     # HEIMAN socket Zigbee (on/off, power measurement)
    'HS3SA': SmokeSensorAdapter,        # HEIMAN Smoke detector    
}