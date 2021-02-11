from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.generic.gas_sensor import GasSensorAdapter
from adapters.generic.smoke_sensor import SmokeSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.lumi.sensor_cube import SensorCube
from adapters.lumi.sensor_motion_aq2 import SensorMotionAq2
from adapters.lumi.DJT11LM import DJT11LM
from adapters.lumi.smart_lock import SmartLock
from adapters.lumi.GZCGQ01LM import GZCGQ01LM
from adapters.lumi.JTYJ_GD_01LM import JTYJ_GD_01LM
from adapters.lumi.WSDCGQ11LM import WSDCGQ11LM
from adapters.lumi.WXCJKG11LM import WXCJKG11LM
from adapters.lumi.WXCJKG12LM import WXCJKG12LM
from adapters.lumi.WXCJKG13LM import WXCJKG13LM
from adapters.lumi.LLKZMK11LM import LLKZMK11LM


lumi_adapters = {
    'A6121': SmartLock,                 # Xiaomi Vima Smart Lock
    'DJT11LM': DJT11LM,                 # Xiaomi Aqara vibration sensor (drop, tilt and touch)
    'GZCGQ01LM': GZCGQ01LM,             # Xiaomi MiJia light intensity sensor
    'JTYJ-GD-01LM/BW': JTYJ_GD_01LM,    # Xiaomi MiJia Honeywell smoke detector
    'JTQJ-BF-01LM/BW': GasSensorAdapter,    # Xiaomi MiJia gas leak detector
    'MFKZQ01LM': SensorCube,            # Xiaomi Mi smart home cube
    'RTCGQ11LM': SensorMotionAq2,       # Xiaomi Aqara human body movement and illuminance sensor
    'WSDCGQ01LM': TemperatureHumiditySensorAdapter, # Xiaomi MiJia temperature & humidity sensor
    'WSDCGQ11LM': WSDCGQ11LM,           # Xiaomi Aqara temperature, humidity and pressure sensor
    'WXCJKG11LM': WXCJKG11LM,           # Xiaomi Aqara Opple 2-button switch
    'WXCJKG12LM': WXCJKG12LM,           # Xiaomi Aqara Opple 4-button switch
    'WXCJKG13LM': WXCJKG13LM,           # Xiaomi Aqara Opple 6-button switch
    'LLKZMK11LM':LLKZMK11LM,            # Xiaomi Aqara Two-way Control Module
}