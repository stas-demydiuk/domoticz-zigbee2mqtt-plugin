from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.contact_adapter import ContactAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.smoke_sensor import SmokeSensorAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.rgbw_adapter import RGBWAdapter
from adapters.cr.gas_sensor import CrGasSensorAdapter as GasAdapter


cr_adapters = {
    'TS0001': OnOffSwitchAdapter,       # CR Smart Home Valve control
    'TS0202': MotionSensorAdapter,      # CR Smart Home Motion sensor
    'TS0203': ContactAdapter,           # CR Smart Home Door sensor
    'TS0205': SmokeSensorAdapter,       # CR Smart Home Smoke sensor
    'TS0111': OnOffSwitchAdapter,       # CR Smart Home Socket
    'TS0204': GasAdapter,               # CR Smart Home Gas sensor
    'TS0207': WaterLeakSensorAdapter,   # CR Smart Home Water leak detector
}
