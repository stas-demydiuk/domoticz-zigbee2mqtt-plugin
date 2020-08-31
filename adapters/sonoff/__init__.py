from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.sonoff.SNZB01 import SNZB01
from adapters.sonoff.SNZB04 import SNZB04


sonoff_adapters = {
    'BASICZBR3': OnOffSwitchAdapter,                # SONOFF Zigbee smart switch
    'S31ZB': OnOffSwitchAdapter,                    # SONOFF Zigbee smart plug (US version)
    'SNZB-01': SNZB01,                              # SONOFF Push switch
    'SNZB-02': TemperatureHumiditySensorAdapter,    # SONOFF Temperature and humidity sensor
    'SNZB-03': MotionSensorAdapter,                 # SONOFF Motion sensor
    'SNZB-04': SNZB04,                              # SONOFF Contact sensor
}
