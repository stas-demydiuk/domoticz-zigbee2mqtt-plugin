from adapters.base_adapter import Adapter
from adapters.contact_adapter import ContactAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.rgb_adapter import RGBAdapter
from adapters.rgbw_adapter import RGBWAdapter
from adapters.ikea.tradfri_wireless_dimmer import TradfriWirelessDimmer
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
from adapters.osram.sensor_motion import SensorMotionOsram
from adapters.samsung.sensor_arrival import SensorArrival
from adapters.philips.hue_dimmer_switch import HueDimmerSwitch
from adapters.philips.hue_motion_sensor import HueMotionSensor

adapter_by_model = {
    # Belkin
    'F7C033': DimmableBulbAdapter,      # Belkin WeMo smart LED bulb
    # Calex
    '421786': DimmableBulbAdapter,      # Calex LED A60 Zigbee GLS-lamp
    # Climax
    'PSS-23ZBS': OnOffSwitchAdapter,    # Climax Power plug
    # Commercial Electric
    '53170161': DimmableCtBulbAdapter,  # Commercial Electric Matte White Recessed Retrofit Smart Led Downlight - 4 Inch
    # Custom devices (DiY)
    'CC2530.ROUTER': Adapter,           # Zigbee router based on CC2530 chip
    'DNCKATSW001': OnOffSwitchAdapter,  # Custom devices (DiY) DNCKAT single key wired wall light switch
    # Dresden Elektronik
    'Mega23M12': RGBWAdapter,           # Dresden Elektronik ZigBee Light Link wireless electronic ballast
    # GE
    '22670': DimmableBulbAdapter,       # GE Link smart LED light bulb, BR30 soft white (2700K)
    '45852GE': DimmableBulbAdapter,     # GE ZigBee plug-in smart dimmer
    '45857GE': DimmableBulbAdapter,     # GE ZigBee in-wall smart dimmer
    # Gledopto
    'GL-C-008': RGBWAdapter,            # Gledopto Zigbee LED controller RGB + CCT / RGBW / WWCW / Dimmer
    # HEIMAN
    'HS1DS': ContactAdapter,            # HEIMAN Door sensor
    # Hive
    'HALIGHTDIMWWE27': DimmableBulbAdapter,     # Hive Active light dimmable
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
    'BY 165': DimmableBulbAdapter,      # Innr B22 Bulb dimmable
    'BY 185 C': RGBWAdapter,            # Innr B22 Bulb RGBW
    'DL 110 N': DimmableBulbAdapter,    # Innr Spot narrow
    'DL 110 W': DimmableBulbAdapter,    # Innr Spot wide
    'PL 110': DimmableBulbAdapter,      # Innr Puck Light
    'RB 145': DimmableBulbAdapter,      # Innr E14 Candle
    'RB 248 T': DimmableCtBulbAdapter,  # Innr E14 Candle with white spectrum
    'RB 165': DimmableBulbAdapter,      # Innr E27 Bulb
    'RB 175 W': DimmableBulbAdapter,    # Innr E27 Bulb warm dimming
    'RB 185 C': RGBWAdapter,            # Innr E27 Bulb RGBW
    'RB 285 C': RGBWAdapter,            # Innr E27 Bulb RGBW
    'RS 125': DimmableBulbAdapter,      # Innr GU10 Spot
    'RS 128 T': DimmableCtBulbAdapter,  # Innr GU10 Spot 350 lm, dimmable, white spectrum
    'SL 110 M': DimmableBulbAdapter,    # Innr Spot Flex medium
    'SL 110 N': DimmableBulbAdapter,    # Innr Spot Flex narrow
    'SL 110 W': DimmableBulbAdapter,    # Innr Spot Flex wide
    'ST 110': DimmableBulbAdapter,      # Innr Strip Light
    'UC 110': DimmableBulbAdapter,      # Innr Under Cabinet Light
    # Iris
    '3210-L': OnOffSwitchAdapter,       # Iris Smart plug
    '3320-L': ContactAdapter,           # Iris Contact sensor
    # JIAWEN
    'K2RGBW01': RGBWAdapter,            # JIAWEN Wireless Bulb E27 9W RGBW
    # Ksentry
    'KS-SM001': OnOffSwitchAdapter,     # Ksentry Electronics Zigbee OnOff Controller
    # Nanoleaf
    'NL08-0800': DimmableBulbAdapter,   # Nanoleaf Ivy smart bulb
    # Nue
    'FB56+ZSW05HG1.2': OnOffSwitchAdapter,      # Nue ZigBee one gang smart switch
    # OSRAM
    'AA68199': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY LED PAR16 50 GU10 tunable white
    'AA69697': RGBWAdapter,             # OSRAM Classic A60 RGBW
    'AA70155': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY LED A19 tunable white / Classic A60 TW
    'AB32840': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY LED Classic B40 tunable white
    'AB35996': RGBWAdapter,             # OSRAM Smart+ Spot GU10 Multicolor
    'AB401130055': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY Surface Light LED Tunable White
    'AB3257001NJ': OnOffSwitchAdapter,  # OSRAM Smart+ plug
    'AC03641': DimmableBulbAdapter,     # OSRAM LIGHTIFY LED Classic A60 clear
    'AC03642': DimmableCtBulbAdapter,   # OSRAM SMART+ CLASSIC A 60 TW
    'AC03645': RGBWAdapter,             # OSRAM LIGHTIFY LED CLA60 E27 RGBW
    'AC08562': DimmableBulbAdapter,     # OSRAM SMART+ Candle E14 Dimmable White
    'AC01353010G': SensorMotionOsram,   # OSRAM SMART+ Motion Sensor
    '4052899926110': RGBWAdapter,       # OSRAM Flex RGBW
    '4052899926158': DimmableBulbAdapter,   # OSRAM LIGHTIFY Surface Light TW
    '4058075036185': RGBWAdapter,       # OSRAM Outdoor Flex RGBW
    '4058075036147': RGBWAdapter,       # OSRAM Smart+ Gardenpole RGBW
    '4058075816718': RGBWAdapter,       # OSRAM SMART+ outdoor wall lantern RGBW
    '4058075816794': DimmableCtBulbAdapter, # OSRAM Smart+ Ceiling TW
    # Paulmann
    '50045': DimmableBulbAdapter,       # Paulmann SmartHome Zigbee LED-stripe
    '50049': RGBAdapter,                # Paulmann SmartHome Yourled RGB Controller
    # Philips
    '3216331P5': DimmableCtBulbAdapter, # Philips Hue white ambiance Aurelle Rectangle Panel Light
    '324131092621': HueDimmerSwitch,    # Philips Hue dimmer switch
    '3261030P7': DimmableCtBulbAdapter, # Philips Hue Being
    '433714': DimmableBulbAdapter,      # Philips Hue Lux A19 bulb E27
    '7146060PH': RGBWAdapter,           # Philips Hue Go
    '7199960PH': RGBAdapter,            # Philips Hue Iris
    '7299355PH': RGBAdapter,            # Philips Hue white and color ambiance LightStrip
    '7299760PH': RGBAdapter,            # Philips Hue Bloom
    '8718696449691': DimmableBulbAdapter,   # Philips Hue white Single bulb B22
    '8718696485880': RGBWAdapter,           # Philips Hue white and color ambiance GU10
    '8718696548738': DimmableCtBulbAdapter, # Philips Hue white ambiance E26/E27
    '8718696598283': DimmableCtBulbAdapter, # Philips Hue white ambiance GU10
    '8718696695203': DimmableCtBulbAdapter, # Philips Hue white ambiance E14
    '915005106701': RGBWAdapter,        # Philips Hue white and color ambiance LightStrip plus
    '915005733701': RGBWAdapter,        # Philips Hue white and color ambiance Play Lightbar
    '9290002579A': RGBWAdapter,         # Philips Hue white and color ambiance BR30
    '9290011370': DimmableBulbAdapter,  # Philips Hue white A60 bulb E27
    '9290012573A': RGBWAdapter,         # Philips Hue white and color ambiance E26/E27 (with Color Temperature)
    '9290012607': HueMotionSensor,      # Philips Hue Motion Sensor (occupancy, temperature, illimination)
    # Sengled
    'E11-G13': DimmableBulbAdapter,     # Sengled Element Classic (A19)
    'E11-G23': DimmableBulbAdapter,     # Sengled Element Classic (A60)
    'E11-N1EA': RGBWAdapter,            # Sengled Element Plus Color (A19)
    'Z01-A19NAE26': DimmableCtBulbAdapter,  # Sengled Element Plus (A19)
    'Z01-CIA19NAE26': DimmableBulbAdapter,  # Sengled Element Touch (A19)
    # SmartThings
    'STSS-MULT-001': ContactAdapter,    # SmartThings SmartSense multi sensor
    'STS-PRS-251': SensorArrival,       # SmartThings SmartThings arrival sensor 
    # Sylvania
    '72922-A': OnOffSwitchAdapter,      # Sylvania SMART+ Smart Plug
    '73693': RGBWAdapter,               # Sylvania LIGHTIFY LED RGBW A19
    '73740': DimmableCtBulbAdapter,     # Sylvania LIGHTIFY LED adjustable white BR30
    '73742': DimmableCtBulbAdapter,     # Sylvania LIGHTIFY LED adjustable white RT 5/6
    '74282': DimmableCtBulbAdapter,     # Sylvania Smart Home adjustable white MR16 LED bulb
    '74283': DimmableBulbAdapter,       # Sylvania LIGHTIFY LED soft white dimmable A19
    '74696': DimmableBulbAdapter,       # Sylvania LIGHTIFY LED soft white dimmable A19
    # Trust
    'ZLED-2709': DimmableBulbAdapter,   # Trust Smart Dimmable LED Bulb
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
