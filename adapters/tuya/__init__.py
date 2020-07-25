from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.tuya.TS0002 import TS0002
from adapters.tuya.TS0012 import TS0012

tuya_adapters = {
    'TS0121': OnOffSwitchAdapter,               # TuYa 10A UK or 16A EU smart plug
    'TS0201': TemperatureHumiditySensorAdapter, # TuYa Temperature & humidity sensor with display
    'TS0002': TS0002,                           # TuYa 2 gang switch
    'TS0012': TS0012,                           # Vrey VR-X711U
}
