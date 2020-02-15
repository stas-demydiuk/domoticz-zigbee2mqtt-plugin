from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.generic.blind_adapter import BlindAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.smoke_sensor import SmokeSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from adapters.lumi.sensor_cube import SensorCube
from adapters.lumi.sensor_magnet import SensorMagnet
from adapters.lumi.sensor_motion_aq2 import SensorMotionAq2
from adapters.lumi.sensor_vibration import SensorVibration
from adapters.lumi.plug import Plug
from adapters.lumi.GZCGQ01LM import GZCGQ01LM
from adapters.lumi.QBKG03LM import QBKG03LM
from adapters.lumi.QBKG12LM import QBKG12LM
from adapters.lumi.JTQJBF01LM import JTQJBF01LM
from adapters.lumi.WSDCGQ11LM import WSDCGQ11LM
from adapters.lumi.WXCJKG12LM import WXCJKG12LM
from adapters.lumi.WXCJKG13LM import WXCJKG13LM
from adapters.lumi.WXKG01LM import WXKG01LM
from adapters.lumi.WXKG02LM import WXKG02LM
from adapters.lumi.WXKG03LM import WXKG03LM
from adapters.lumi.WXKG11LM import WXKG11LM
from adapters.lumi.WXKG12LM import WXKG12LM
from adapters.lumi.ZNCZ02LM import ZNCZ02KM
from adapters.lumi.LLKZMK11LM import LLKZMK11LM

lumi_adapters = {
    'DJT11LM': SensorVibration,         # Xiaomi Aqara vibration sensor (drop, tilt and touch)
    'GZCGQ01LM': GZCGQ01LM,             # Xiaomi MiJia light intensity sensor
    'JTYJ-GD-01LM/BW': SmokeSensorAdapter,  # Xiaomi MiJia Honeywell smoke detector
    'JTQJ-BF-01LM/BW': JTQJBF01LM,      # Xiaomi MiJia gas leak detector
    'MCCGQ01LM': SensorMagnet,          # Xiaomi MiJia door & window contact sensor
    'MCCGQ11LM': SensorMagnet,          # Xiaomi Aqara door & window contact sensor
    'MFKZQ01LM': SensorCube,            # Xiaomi Mi smart home cube
    'QBCZ11LM': Plug,                   # Xiaomi Aqara socket Zigbee (on/off, power measurement)
    'QBKG03LM': QBKG03LM,               # Xiaomi Aqara double key wired wall switch
    'QBKG04LM': OnOffSwitchAdapter,     # Xiaomi Aqara single key wired wall switch
    'QBKG11LM': Plug,                   # Xiaomi Aqara single key wired wall switch
    'QBKG12LM': QBKG12LM,               # Xiaomi Aqara double key wired wall switch
    'RTCGQ01LM': MotionSensorAdapter,   # Xiaomi MiJia human body movement sensor
    'RTCGQ11LM': SensorMotionAq2,       # Xiaomi Aqara human body movement and illuminance sensor
    'SJCGQ11LM': WaterLeakSensorAdapter,# Xiaomi Aqara water leak sensor
    'WSDCGQ01LM': TemperatureHumiditySensorAdapter, # Xiaomi MiJia temperature & humidity sensor
    'WSDCGQ11LM': WSDCGQ11LM,           # Xiaomi Aqara temperature, humidity and pressure sensor
    'WXCJKG12LM': WXCJKG12LM,           # Xiaomi Aqara Opple 4-button switch
    'WXCJKG13LM': WXCJKG13LM,           # Xiaomi Aqara Opple 6-button switch
    'WXKG01LM': WXKG01LM,               # Xiaomi MiJia wireless switch
    'WXKG02LM': WXKG02LM,               # Xiaomi Aqara double key wireless wall switch
    'WXKG03LM': WXKG03LM,               # Xiaomi Aqara single key wireless wall switch
    'WXKG11LM': WXKG11LM,               # Xiaomi Aqara wireless switch
    'WXKG12LM': WXKG12LM,               # Xiaomi Aqara wireless switch (with gyroscope)
    'ZNCZ02LM': ZNCZ02KM,               # Xiaomi Mi power plug ZigBee
    'ZNCZ04LM': Plug,                   # Xiaomi Mi power plug ZigBee EU
    'ZNCLDJ11LM': BlindAdapter,         # Xiaomi Aqara curtain motor
    'ZNCLDJ12LM': BlindAdapter,         # Xiaomi Aqara B1 curtain motor
    'ZNLDP12LM': DimmableCtBulbAdapter, # Xiaomi Aqara smart LED bulb
    'LLKZMK11LM':LLKZMK11LM,            # Xiaomi Aqara Two-way Control Module
}