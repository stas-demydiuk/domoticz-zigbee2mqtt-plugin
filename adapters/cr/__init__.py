from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.smoke_sensor import SmokeSensorAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from adapters.cr.gas_sensor import CrGasSensorAdapter as GasAdapter


cr_adapters = {
    'TS0202': MotionSensorAdapter,      # CR Smart Home Motion sensor
    'TS0205': SmokeSensorAdapter,       # CR Smart Home Smoke sensor
    'TS0204': GasAdapter,               # CR Smart Home Gas sensor
    'TS0207': WaterLeakSensorAdapter,   # CR Smart Home Water leak detector
}
