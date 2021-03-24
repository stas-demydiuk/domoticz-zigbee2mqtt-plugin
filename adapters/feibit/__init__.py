from adapters.generic.gas_sensor import GasSensorAdapter
from adapters.heiman.HS1CAE import HS1CAE


feibit_adapters = {
    'SCA01ZB': HS1CAE,                              # Feibit Smart carbon monoxide sensor
    'SGA01ZB': GasSensorAdapter,                    # Feibit Combustible gas sensor
}