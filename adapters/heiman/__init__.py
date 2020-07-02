from adapters.contact_adapter import ContactAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.smoke_sensor import SmokeSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter as TempHumAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from adapters.generic.on_off_kwh import OnOffKwhAdapter
from adapters.generic.siren import SirenAdapterWithBattery
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.heiman.gas_sensor import HeimanGasSensorAdapter as GasAdapter
from adapters.heiman.HS1CAE import HS1CAE
from adapters.heiman.HS1WLE import HS1WLE
from adapters.heiman.HS2SK import HS2SK
from adapters.heiman.SMHMI1 import SMHMI1


heiman_adapters = {
    'HM-900SW_1': OnOffSwitchAdapter,   # HEIMAN Smart switch - 1 gang with neutral wire
    'HS1-WL-E': HS1WLE,                 # HEIMAN Water leakage sensor
    'HS1CA-E': HS1CAE,                  # HEIMAN Monoxyde detector
    'HS1CA-M': HS1CAE,                  # HEIMAN Monoxyde detector
    'HS1DS': ContactAdapter,            # HEIMAN Door sensor
    'HS1DS-E': ContactAdapter,          # HEIMAN Door sensor
    'HS1HT': TempHumAdapter,            # HEIMAN Smart temperature & humidity Sensor
    'HS1SA': SmokeSensorAdapter,        # HEIMAN Smoke detector
    'HS1SA-M': SmokeSensorAdapter,      # HEIMAN Smoke detector
    'HS1WL': WaterLeakSensorAdapter,    # HEIMAN Water leakage sensor
    'HS2ESK-E': OnOffKwhAdapter,        # HEIMAN Smart in wall plug
    'HS2SK': HS2SK,                     # HEIMAN Smart metering plug
    'HS2WD-E': SirenAdapterWithBattery, # HEIMAN Smart siren
    'HS3MS': MotionSensorAdapter,       # HEIMAN Smart motion sensor
    'HS3SA': SmokeSensorAdapter,        # HEIMAN Smoke detector
    'SKHMP30-I1': HS2SK,                # HEIMAN Smart metering plug
    'SMHM-I1': SMHMI1,                  # HEIMAN Smart motion sensor
    'SOHM-I1': ContactAdapter,          # HEIMAN Door contact sensor
    'STHM-I1H': TempHumAdapter,         # HEIMAN temperature & humidity sensor
    'SWHM-I1': WaterLeakSensorAdapter,  # HEIMAN Water leakage sensor
    'HS3CG': GasAdapter,                # HEIMAN Combustible gas sensor
    'HS1CG-E': GasAdapter,              # HEIMAN Combustible gas sensor
    'HS1CG-M': GasAdapter,              # HEIMAN Combustible gas sensor
    'HS1CG_M': GasAdapter,              # HEIMAN Combustible gas sensor
    'SGMHM-I1': GasAdapter,             # HEIMAN Combustible gas sensor
    'FS1RG': GasAdapter,                # Ferguson Combustible gas sensor
}
