from adapters.generic.gas_sensor import GasSensorAdapter
from adapters.generic.smoke_sensor import SmokeSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.heiman.HS1CAE import HS1CAE


feibit_adapters = {
    'SCA01ZB': HS1CAE,                              # Feibit Smart carbon monoxide sensor
    'SGA01ZB': GasSensorAdapter,                    # Feibit Combustible gas sensor
    'SSA01ZB': SmokeSensorAdapter,                  # Feibit Smoke detector
    'STH01ZB': TemperatureHumiditySensorAdapter,    # Feibit Smart temperature & humidity Sensor
}