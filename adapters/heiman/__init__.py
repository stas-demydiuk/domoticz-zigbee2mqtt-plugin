from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter as TempHumAdapter
from adapters.generic.siren import SirenAdapterWithBattery
from adapters.heiman.gas_sensor import HeimanGasSensorAdapter as GasAdapter
from adapters.heiman.HS1CAE import HS1CAE
from adapters.heiman.HS1RC import HeimanAlarmRemoteAdapter


heiman_adapters = {
    'HS1CA-E': HS1CAE,                  # HEIMAN Monoxyde detector
    'HS1CA-M': HS1CAE,                  # HEIMAN Monoxyde detector
    'HS1HT': TempHumAdapter,            # HEIMAN Smart temperature & humidity Sensor
    'HS2WD-E': SirenAdapterWithBattery, # HEIMAN Smart siren
    'STHM-I1H': TempHumAdapter,         # HEIMAN temperature & humidity sensor
    'HS3CG': GasAdapter,                # HEIMAN Combustible gas sensor
    'HS1CG-E': GasAdapter,              # HEIMAN Combustible gas sensor
    'HS1CG-M': GasAdapter,              # HEIMAN Combustible gas sensor
    'HS1CG_M': GasAdapter,              # HEIMAN Combustible gas sensor
    'SGMHM-I1': GasAdapter,             # HEIMAN Combustible gas sensor
    'FS1RG': GasAdapter,                # Ferguson Combustible gas sensor
	'HS1RC-EM': HeimanAlarmRemoteAdapter, # HEIMAN Alarm remote
}
