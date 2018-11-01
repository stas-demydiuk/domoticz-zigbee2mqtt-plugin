from adapters.nanoleaf.NL08_0800 import NL08_0800
from adapters.ikea.tradfri_color_light import TradfriColorLight
from adapters.ikea.tradfri_dimmable_bulb import TradfriDimmableBulb
from adapters.ikea.tradfri_wireless_dimmer import TradfriWirelessDimmer
from adapters.lumi.sensor_cube import SensorCube
from adapters.lumi.sensor_magnet import SensorMagnet
from adapters.lumi.sensor_motion import SensorMotion
from adapters.lumi.sensor_motion_aq2 import SensorMotionAq2
from adapters.lumi.sensor_temp_hum import SensorTemperatureHumidity
from adapters.lumi.sensor_vibration import SensorVibration
from adapters.lumi.sensor_wleak import SensorWleak
from adapters.lumi.plug import Plug
from adapters.lumi.ctrl_neutral2 import AqaraDoubleWiredSwitch
from adapters.lumi.WXKG01LM import WXKG01LM
from adapters.lumi.WXKG02LM import WXKG02LM
from adapters.lumi.WXKG03LM import WXKG03LM
from adapters.lumi.WXKG11LM import WXKG11LM
from adapters.lumi.WXKG12LM import WXKG12LM
from adapters.lumi.weather import Weather

adapter_by_model = {
    'NL08-0800': NL08_0800,             # Nanoleaf Ivy smart bulb
    'LED1622G12': TradfriDimmableBulb,  # IKEA TRADFRI LED bulb E26 1000 lumen, dimmable, opal white 
    'LED1623G12': TradfriDimmableBulb,  # IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, opal white
    'LED1624G9': TradfriColorLight,     # IKEA TRADFRI LED bulb E27 600 lumen, dimmable, color, opal white
    'LED1649C5': TradfriDimmableBulb,   # IKEA TRADFRI LED bulb E14 400 lumen, dimmable warm white, chandelier opal
    'LED1650R5': TradfriDimmableBulb,   # IKEA TRADFRI LED bulb GU10 400 lumen, dimmable
    'ICTC-G-1': TradfriWirelessDimmer,  # IKEA TRADFRI wireless dimmer
    'ZNCZ02LM': Plug,                   # Xiaomi Mi power plug ZigBee
    'QBCZ11LM': Plug,                   # Xiaomi Aqara socket Zigbee (on/off, power measurement)
    'MFKZQ01LM': SensorCube,            # Xiaomi Mi smart home cube
    'WXKG02LM': WXKG02LM,               # Xiaomi Aqara double key wireless wall switch
    'WXKG03LM': WXKG03LM,               # Xiaomi Aqara single key wireless wall switch
    'MCCGQ01LM': SensorMagnet,          # Xiaomi MiJia door & window contact sensor
    'MCCGQ11LM': SensorMagnet,          # Xiaomi Aqara door & window contact sensor
    'RTCGQ01LM': SensorMotion,          # Xiaomi MiJia human body movement sensor
    'RTCGQ11LM': SensorMotionAq2,       # Xiaomi Aqara human body movement and illuminance sensor 
    'WXKG01LM': WXKG01LM,               # Xiaomi MiJia wireless switch
    'WXKG11LM': WXKG11LM,               # Xiaomi Aqara wireless switch
    'WXKG12LM': WXKG12LM,               # Xiaomi Aqara wireless switch (with gyroscope)
    'SJCGQ11LM': SensorWleak,           # Xiaomi Aqara water leak sensor
    'QBKG03LM': AqaraDoubleWiredSwitch, # Xiaomi Aqara double key wired wall switch
    'QBKG12LM': AqaraDoubleWiredSwitch, # Xiaomi Aqara double key wired wall switch
    'WSDCGQ01LM': SensorTemperatureHumidity,    # Xiaomi MiJia temperature & humidity sensor
    'WSDCGQ11LM': Weather,              # Xiaomi Aqara temperature, humidity and pressure sensor 
    'DJT11LM': SensorVibration          # Xiaomi Aqara vibration sensor (drop, tilt and touch)
}