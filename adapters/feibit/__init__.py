from adapters.contact_adapter import ContactAdapter
from adapters.generic.gas_sensor import GasSensorAdapter
from adapters.generic.smoke_sensor import SmokeSensorAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.heiman.HS1CAE import HS1CAE


feibit_adapters = {
    'SCA01ZB': HS1CAE,                              # Feibit Smart carbon monoxide sensor
    'SDM01ZB': ContactAdapter,                      # Feibit Door or window contact switch
    'SFS01ZB': OnOffSwitchAdapter,                  # Feibit Power plug
    'SGA01ZB': GasSensorAdapter,                    # Feibit Combustible gas sensor
    'SSA01ZB': SmokeSensorAdapter,                  # Feibit Smoke detector
    'STH01ZB': TemperatureHumiditySensorAdapter,    # Feibit Smart temperature & humidity Sensor
    'SWA01ZB': WaterLeakSensorAdapter,              # Feibit Water leakage sensor
}