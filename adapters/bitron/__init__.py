from adapters.generic.on_off_kwh import OnOffKwhAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.bitron.AV201032 import AV201032


bitron_adapters = {
    'AV2010/22': MotionSensorAdapter,   # Bitron Wireless motion detector
    'AV2010/25': OnOffKwhAdapter,       # Bitron Wireless smart plug
    'AV2010/32': AV201032,              # Bitron Wireless wall thermostat with relay
}
