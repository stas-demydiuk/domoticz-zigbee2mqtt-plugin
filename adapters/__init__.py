from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.ikea.tradfri_color_light import TradfriColorLight
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
    'F7C033': DimmableBulbAdapter,      # Belkin WeMo smart LED bulb
    'DNCKATSW001': OnOffSwitchAdapter,  # Custom devices (DiY) DNCKAT single key wired wall light switch
    'HALIGHTDIMWWE27': DimmableBulbAdapter,     # Hive Active light dimmable
    '3210-L': OnOffSwitchAdapter,       # Iris Smart plug
    'KS-SM001': OnOffSwitchAdapter,     # Ksentry Electronics Zigbee OnOff Controller
    'NL08-0800': DimmableBulbAdapter,   # Nanoleaf Ivy smart bulb
    'FB56+ZSW05HG1.2': OnOffSwitchAdapter,      # Nue ZigBee one gang smart switch
    '50045': DimmableBulbAdapter,       # Paulmann SmartHome Zigbee LED-stripe
    'ZLED-2709': DimmableBulbAdapter,   # Trust Smart Dimmable LED Bulb
    # GE
    '22670': DimmableBulbAdapter,       # GE Link smart LED light bulb, BR30 soft white (2700K)
    '45852GE': DimmableBulbAdapter,     # GE ZigBee plug-in smart dimmer
    '45857GE': DimmableBulbAdapter,     # GE ZigBee in-wall smart dimmer
    # Ikea
    'LED1622G12': DimmableBulbAdapter,  # IKEA TRADFRI LED bulb E26 1000 lumen, dimmable, opal white 
    'LED1623G12': DimmableBulbAdapter,  # IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, opal white
    'LED1624G9': TradfriColorLight,     # IKEA TRADFRI LED bulb E27 600 lumen, dimmable, color, opal white
    'LED1649C5': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb E14 400 lumen, dimmable warm white, chandelier opal
    'LED1650R5': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb GU10 400 lumen, dimmable
    'ICPSHC24-10EU-IL-1': DimmableBulbAdapter,  # IKEA TRADFRI driver for wireless control (10 watt)
    'ICPSHC24-30EU-IL-1': DimmableBulbAdapter,  # IKEA TRADFRI driver for wireless control (30 watt)
    'ICTC-G-1': TradfriWirelessDimmer,  # IKEA TRADFRI wireless dimmer
    'E1603': OnOffSwitchAdapter,        # IKEA TRADFRI control outlet
    # Innr
    'RB 165': DimmableBulbAdapter,      # Innr E27 Bulb
    'RB 175 W': DimmableBulbAdapter,    # Innr E27 Bulb warm dimming
    'RS 125': DimmableBulbAdapter,      # Innr GU10 Spot
    'RB 145': DimmableBulbAdapter,      # Innr E14 Candle
    'BY 165': DimmableBulbAdapter,      # Innr B22 Bulb dimmable
    'PL 110': DimmableBulbAdapter,      # Innr Puck Light
    'ST 110': DimmableBulbAdapter,      # Innr Strip Light
    'UC 110': DimmableBulbAdapter,      # Innr Under Cabinet Light
    'DL 110 N': DimmableBulbAdapter,    # Innr Spot narrow
    'DL 110 W': DimmableBulbAdapter,    # Innr Spot wide
    'SL 110 N': DimmableBulbAdapter,    # Innr Spot Flex narrow
    'SL 110 M': DimmableBulbAdapter,    # Innr Spot Flex medium
    'SL 110 W': DimmableBulbAdapter,    # Innr Spot Flex wide
    # OSRAM
    'AB3257001NJ': OnOffSwitchAdapter,  # OSRAM Smart+ plug
    'AC03641': DimmableBulbAdapter,     # OSRAM LIGHTIFY LED Classic A60 clear
    # Philips
    '324131092621': OnOffSwitchAdapter, # Philips Hue dimmer switch
    '433714': DimmableBulbAdapter,      # Philips Hue Lux A19 bulb E27
    '9290011370': DimmableBulbAdapter,  # Philips Hue white A60 bulb E27
    '8718696449691': DimmableBulbAdapter,   # Philips Hue White Single bulb B22
    # Sengled
    'E11-G13': DimmableBulbAdapter,     # Sengled Element Classic (A19)
    'E11-G23': DimmableBulbAdapter,     # Sengled Element Classic (A60)
    'Z01-CIA19NAE26': DimmableBulbAdapter,  # Sengled Element Touch (A19)
    # Sylvania
    '74283': DimmableBulbAdapter,       # Sylvania LIGHTIFY LED soft white dimmable A19
    '74696': DimmableBulbAdapter,       # Sylvania LIGHTIFY LED soft white dimmable A19
    '72922-A': OnOffSwitchAdapter,      # Sylvania SMART+ Smart Plug
    # Xiaomi
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
    'QBKG04LM': OnOffSwitchAdapter,     # Xiaomi Aqara single key wired wall switch
    'QBKG12LM': AqaraDoubleWiredSwitch, # Xiaomi Aqara double key wired wall switch
    'WSDCGQ01LM': SensorTemperatureHumidity,    # Xiaomi MiJia temperature & humidity sensor
    'WSDCGQ11LM': Weather,              # Xiaomi Aqara temperature, humidity and pressure sensor 
    'DJT11LM': SensorVibration          # Xiaomi Aqara vibration sensor (drop, tilt and touch)
}