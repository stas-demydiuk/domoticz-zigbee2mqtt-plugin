from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.tuyatec.GDKES02TZXD import GDKES02TZXD
from adapters.tuyatec.GDKES03TZXD import GDKES03TZXD

tuyatec_adapters = {
    'RH3040': MotionSensorAdapter,                  # TUYATEC PIR sensor
    'TT001ZAV20': TemperatureHumiditySensorAdapter, # TUYATEC Temperature & humidity sensor
    'GDKES-01TZXD': OnOffSwitchAdapter,             # TUYATEC Smart light switch - 1 gang without neutral wire
    'gq8b1uv': DimmableBulbAdapter,                 # TUYATEC Zigbee smart dimmer
    'GDKES-02TZXD': GDKES02TZXD,                   # TUYATEC Smart light switch - 2 gangs without neutral
    'GDKES-03TZXD': GDKES03TZXD,                    # TUYATEC Smart light switch - 3 gangs without neutral
}
