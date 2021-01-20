from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.tuyatec.GDKES02TZXD import GDKES02TZXD
from adapters.tuyatec.GDKES03TZXD import GDKES03TZXD

tuyatec_adapters = {
    'RH3040': MotionSensorAdapter,                  # TUYATEC PIR sensor
    'TT001ZAV20': TemperatureHumiditySensorAdapter, # TUYATEC Temperature & humidity sensor
    'GDKES-02TZXD': GDKES02TZXD,                   # TUYATEC Smart light switch - 2 gangs without neutral
    'GDKES-03TZXD': GDKES03TZXD,                    # TUYATEC Smart light switch - 3 gangs without neutral
}
