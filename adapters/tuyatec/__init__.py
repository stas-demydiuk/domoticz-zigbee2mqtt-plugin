from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter


tuyatec_adapters = {
    'RH3040': MotionSensorAdapter,                  # TUYATEC PIR sensor
    'TT001ZAV20': TemperatureHumiditySensorAdapter, # TUYATEC Temperature & humidity sensor
    'GDKES-01TZXD': OnOffSwitchAdapter,             # TUYATEC Smart light switch - 1 gang without neutral wire
    'gq8b1uv': DimmableBulbAdapter,                 # TUYATEC Zigbee smart dimmer
    'TS0201': TemperatureHumiditySensorAdapter,     # TUYATEC Temperature & humidity sensor with display
}