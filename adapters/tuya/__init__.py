from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.tuya.TS0002 import TS0002

tuya_adapters = {
    'TS0201': TemperatureHumiditySensorAdapter, # TuYa Temperature & humidity sensor with display
    'TS0002': TS0002,                           # TuYa 2 gang switch
}
