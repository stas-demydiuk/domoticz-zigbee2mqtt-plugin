from adapters.base_adapter import Adapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.rgb_adapter import RGBAdapter
from adapters.rgbw_adapter import RGBWAdapter
from adapters.ikea.tradfri_wireless_dimmer import TradfriWirelessDimmer
from adapters.innr.SP120 import InnrSP120Plug
from adapters.lumi.sensor_cube import SensorCube
from adapters.lumi.sensor_magnet import SensorMagnet
from adapters.lumi.sensor_motion import SensorMotion
from adapters.lumi.sensor_motion_aq2 import SensorMotionAq2
from adapters.lumi.sensor_smoke import SensorSmoke
from adapters.lumi.sensor_vibration import SensorVibration
from adapters.lumi.sensor_wleak import SensorWleak
from adapters.lumi.plug import Plug
from adapters.lumi.ctrl_neutral2 import AqaraDoubleWiredSwitch
from adapters.lumi.WSDCGQ01LM import WSDCGQ01LM
from adapters.lumi.WSDCGQ11LM import WSDCGQ11LM
from adapters.lumi.WXKG01LM import WXKG01LM
from adapters.lumi.WXKG02LM import WXKG02LM
from adapters.lumi.WXKG03LM import WXKG03LM
from adapters.lumi.WXKG11LM import WXKG11LM
from adapters.lumi.WXKG12LM import WXKG12LM
from adapters.samsung.sensor_contact import SensorContact
from adapters.samsung.sensor_arrival import SensorArrival

adapter_by_model = {
    'CC2530.ROUTER': Adapter,           # Zigbee router based on CC2530 chip
    'F7C033': DimmableBulbAdapter,      # Belkin WeMo smart LED bulb
    '53170161': DimmableCtBulbAdapter,  # Commercial Electric Matte White Recessed Retrofit Smart Led Downlight - 4 Inch
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
    # Gledopto
    'GL-C-008': RGBWAdapter,            # Gledopto Zigbee LED controller RGB + CCT / RGBW / WWCW / Dimmer
    # Ikea
    'LED1536G5': DimmableCtBulbAdapter, # IKEA TRADFRI LED bulb E12/E14 400 lumen, dimmable, white spectrum, opal white
    'LED1537R6': DimmableCtBulbAdapter, # IKEA TRADFRI LED bulb GU10 400 lumen, dimmable, white spectrum
    'LED1545G12': DimmableCtBulbAdapter,# IKEA TRADFRI LED bulb E26/E27 980 lumen, dimmable, white spectrum, opal white
    'LED1546G12': DimmableCtBulbAdapter,# IKEA TRADFRI LED bulb E26/E27 950 lumen, dimmable, white spectrum, clear
    'LED1622G12': DimmableBulbAdapter,  # IKEA TRADFRI LED bulb E26 1000 lumen, dimmable, opal white 
    'LED1623G12': DimmableBulbAdapter,  # IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, opal white
    'LED1624G9': RGBAdapter,            # IKEA TRADFRI LED bulb E27 600 lumen, dimmable, color, opal white
    'LED1649C5': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb E14 400 lumen, dimmable warm white, chandelier opal
    'LED1650R5': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb GU10 400 lumen, dimmable
    'ICPSHC24-10EU-IL-1': DimmableBulbAdapter,  # IKEA TRADFRI driver for wireless control (10 watt)
    'ICPSHC24-30EU-IL-1': DimmableBulbAdapter,  # IKEA TRADFRI driver for wireless control (30 watt)
    'ICTC-G-1': TradfriWirelessDimmer,  # IKEA TRADFRI wireless dimmer
    'L1527': DimmableCtBulbAdapter,     # IKEA FLOALT LED light panel, dimmable, white spectrum (30x30 cm)
    'L1528': DimmableCtBulbAdapter,     # IKEA FLOALT LED light panel, dimmable, white spectrum (30x90 cm)
    'L1529': DimmableCtBulbAdapter,     # IKEA FLOALT LED light panel, dimmable, white spectrum (60x60 cm)
    'E1603': OnOffSwitchAdapter,        # IKEA TRADFRI control outlet
    # Innr
    'RB 165': DimmableBulbAdapter,      # Innr E27 Bulb
    'RB 175 W': DimmableBulbAdapter,    # Innr E27 Bulb warm dimming
    'RS 125': DimmableBulbAdapter,      # Innr GU10 Spot
    'RS 128 T': DimmableCtBulbAdapter,  # Innr GU10 Spot 350 lm, dimmable, white spectrum
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
    'SP 120': InnrSP120Plug,
    # OSRAM
    'AC03641': DimmableBulbAdapter,     # OSRAM LIGHTIFY LED Classic A60 clear
    'AC03642': DimmableCtBulbAdapter,   # OSRAM SMART+ CLASSIC A 60 TW
    'AA70155': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY LED A19 tunable white / Classic A60 TW
    'AA68199': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY LED PAR16 50 GU10 tunable white
    'AB32840': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY LED Classic B40 tunable white
    'AB401130055': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY Surface Light LED Tunable White
    'AB3257001NJ': OnOffSwitchAdapter,  # OSRAM Smart+ plug
    # Philips
    '7299760PH': RGBAdapter,            # Philips Hue Bloom
    '324131092621': OnOffSwitchAdapter, # Philips Hue dimmer switch
    '433714': DimmableBulbAdapter,      # Philips Hue Lux A19 bulb E27
    '9290011370': DimmableBulbAdapter,  # Philips Hue white A60 bulb E27
    '8718696449691': DimmableBulbAdapter,   # Philips Hue White Single bulb B22
    '8718696695203': DimmableCtBulbAdapter, # Philips Hue white ambiance E14
    '8718696598283': DimmableCtBulbAdapter, # Philips Hue white ambiance GU10
    '8718696548738': DimmableCtBulbAdapter, # Philips Hue white ambiance E26/E27
    '3261030P7': DimmableCtBulbAdapter, # Philips Hue Being
    '7299355PH': RGBAdapter,            # Philips Hue white and color ambiance LightStrip
    '7199960PH': RGBAdapter,            # Philips Hue Iris
    '9290012573A': RGBWAdapter,         # Philips Hue white and color ambiance E26/E27 (with Color Temperature)
    # Sengled
    'E11-G13': DimmableBulbAdapter,     # Sengled Element Classic (A19)
    'E11-G23': DimmableBulbAdapter,     # Sengled Element Classic (A60)
    'Z01-CIA19NAE26': DimmableBulbAdapter,  # Sengled Element Touch (A19)
    # SmartThings
    'STSS-MULT-001': SensorContact,     # SmartThings SmartSense multi sensor
    'STS-PRS-251': SensorArrival,       # SmartThings SmartThings arrival sensor 
    # Sylvania
    '73742': DimmableCtBulbAdapter,     # Sylvania LIGHTIFY LED adjustable white RT 5/6
    '73740': DimmableCtBulbAdapter,     # Sylvania LIGHTIFY LED adjustable white BR30
    '74282': DimmableCtBulbAdapter,     # Sylvania Smart Home adjustable white MR16 LED bulb
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
    'WSDCGQ01LM': WSDCGQ01LM,           # Xiaomi MiJia temperature & humidity sensor
    'WSDCGQ11LM': WSDCGQ11LM,           # Xiaomi Aqara temperature, humidity and pressure sensor 
    'DJT11LM': SensorVibration,         # Xiaomi Aqara vibration sensor (drop, tilt and touch)
    'JTYJ-GD-01LM/BW': SensorSmoke      # Xiaomi MiJia Honeywell smoke detector
}
