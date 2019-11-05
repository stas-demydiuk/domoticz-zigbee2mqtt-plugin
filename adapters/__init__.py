from adapters.base_adapter import Adapter
from adapters.contact_adapter import ContactAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.rgb_adapter import RGBAdapter
from adapters.rgbw_adapter import RGBWAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.motion_temp_sensor import MotionAndTemperatureSensorAdapter
from adapters.generic.on_off_kwh import OnOffKwhAdapter
from adapters.generic.smoke_sensor import SmokeSensorAdapter
from adapters.generic.temperature_sensor import TemperatureSensorAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from adapters.gira.light_link import GiraLightLink
from adapters.heiman.HS1WLE import HS1WLE
from adapters.heiman.HS2SK import HS2SK
from adapters.ikea.tradfri_remote_control import TradfriRemoteControl
from adapters.ikea.tradfri_wireless_dimmer import TradfriWirelessDimmer
from adapters.ikea.tradfri_switch_on_off import TradfriRemoteSwitchOnOff
from adapters.ikea.tradfri_remote_close_open import TradfriRemoteCloseOpen
from adapters.ikea.tradfri_roller_blind import TradfriRollerBlind
from adapters.innr.SP120 import InnrSP120Plug
from adapters.konke.button import KonkeButton
from adapters.konke.sensor_temp_hum import KonkeTemperatureHumiditySensor
from adapters.livolo.TI0001 import TI0001
from adapters.lumi.sensor_cube import SensorCube
from adapters.lumi.sensor_magnet import SensorMagnet
from adapters.lumi.sensor_motion_aq2 import SensorMotionAq2
from adapters.lumi.sensor_vibration import SensorVibration
from adapters.lumi.plug import Plug
from adapters.lumi.ctrl_neutral2 import AqaraDoubleWiredSwitch
from adapters.lumi.JTQJBF01LM import JTQJBF01LM
from adapters.lumi.WSDCGQ01LM import WSDCGQ01LM
from adapters.lumi.WSDCGQ11LM import WSDCGQ11LM
from adapters.lumi.WXKG01LM import WXKG01LM
from adapters.lumi.WXKG02LM import WXKG02LM
from adapters.lumi.WXKG03LM import WXKG03LM
from adapters.lumi.WXKG11LM import WXKG11LM
from adapters.lumi.WXKG12LM import WXKG12LM
from adapters.lumi.ZNCZ02LM import ZNCZ02KM
from adapters.lumi.LLKZMK11LM import LLKZMK11LM
from adapters.samsung.sensor_arrival import SensorArrival
from adapters.samsung.sensor_door import SmartThingsDoorSensor
from adapters.philips.hue_dimmer_switch import HueDimmerSwitch
from adapters.philips.hue_motion_sensor import HueMotionSensor
from adapters.swo.KEF1PA import KEF1PA
from adapters.thermostat import ThermostatAdapter

adapter_by_model = {
    # AduroSmart
    '81809': RGBWAdapter,               # AduroSmart ERIA colors and white shades smart light bulb A19
    # Airam
    '4713407': DimmableBulbAdapter,     # Airam LED OP A60 ZB 9W/827 E27
    # Anchor
    '67200BL': OnOffSwitchAdapter,      # Anchor Vetaar smart plug
    # Belkin
    'F7C033': DimmableBulbAdapter,      # Belkin WeMo smart LED bulb
    # Bitron
    'AV2010/22': MotionSensorAdapter,   # Bitron Wireless motion detector
    'AV2010/25': OnOffKwhAdapter,       # Bitron Wireless smart plug
    # Bosch
    'RADON TriTech ZB': MotionAndTemperatureSensorAdapter,  # Bosch Wireless motion detector
    'ISW-ZPR1-WP13': MotionAndTemperatureSensorAdapter,     # Bosch Motion sensor
    # Calex
    '421786': DimmableBulbAdapter,      # Calex LED A60 Zigbee GLS-lamp
    # Climax
    'PSS-23ZBS': OnOffSwitchAdapter,    # Climax Power plug
    # Commercial Electric
    '53170161': DimmableCtBulbAdapter,  # Commercial Electric Matte White Recessed Retrofit Smart Led Downlight - 4 Inch
    # Connex
    'ZG9101SAC-HP': DimmableBulbAdapter,# CONNEX Zigbee Phasendimmer 230V bis 400W
    # Custom devices (DiY)
    'CC2530.ROUTER': Adapter,           # Zigbee router based on CC2530 chip
    'DNCKATSW001': OnOffSwitchAdapter,  # Custom devices (DiY) DNCKAT single key wired wall light switch
    # Dresden Elektronik
    'Mega23M12': RGBWAdapter,           # Dresden Elektronik ZigBee Light Link wireless electronic ballast
    'XVV-Mega23M12': DimmableCtBulbAdapter, # Dresden Elektronik ZigBee Light Link wireless electronic ballast color temperature
    # EcoSmart
    'D1531': DimmableBulbAdapter,       # EcoSmart A19 bright white bulb
    'D1532': DimmableBulbAdapter,       # EcoSmart A19 soft white bulb (on/off, brightness)
    'D1821': RGBWAdapter,               # EcoSmart A19 RGB bulb (on/off, brightness, color temperature, color xy)
    # GE
    '22670': DimmableBulbAdapter,       # GE Link smart LED light bulb, BR30 soft white (2700K)
    '45852GE': DimmableBulbAdapter,     # GE ZigBee plug-in smart dimmer
    '45853GE': OnOffSwitchAdapter,      # GE ZigBee plug-in smart switch
    '45856GE': OnOffSwitchAdapter,      # GE ZigBee in-wall smart switch
    '45857GE': DimmableBulbAdapter,     # GE ZigBee in-wall smart dimmer
    # Gira
    '2430-100': GiraLightLink,          # Gira ZigBee Light Link wall transmitter
    # Gledopto
    'GD-CZ-006': DimmableBulbAdapter,   # Gledopto Zigbee LED Driver
    'GL-B-007Z': RGBWAdapter,           # Gledopto Smart 6W E27 RGB / CW LED bulb
    'GL-B-008Z': RGBWAdapter,           # Gledopto Smart 12W E27 RGB / CW LED bulb
    'GL-C-006': DimmableCtBulbAdapter,  # Gledopto Zigbee LED controller WW/CW Dimmer
    'GL-C-008': RGBWAdapter,            # Gledopto Zigbee LED controller RGB + CCT / RGBW / WWCW / Dimmer
    'GL-D-003Z': RGBWAdapter,           # Gledopto LED RGB + CCT downlight
    'GL-FL-004TZ': RGBWAdapter,         # Gledopto Zigbee 10W floodlight RGB CCT
    'GL-MC-001': RGBWAdapter,           # Gledopto Zigbee USB mini LED controller RGB + CCT
    'GL-S-003Z': RGBWAdapter,           # Gledopto Smart RGBW GU10
    'GL-S-004Z': DimmableCtBulbAdapter, # Gledopto Smart Wnite GU10
    'GL-S-007Z': RGBWAdapter,           # Gledopto Smart RGBW GU10
    # HEIMAN
    'HS1DS': ContactAdapter,            # HEIMAN Door sensor
    'HS1DS-E': ContactAdapter,          # HEIMAN Door sensor
    'HS1SA': SmokeSensorAdapter,        # HEIMAN Smoke detector
    'HS1WL': WaterLeakSensorAdapter,    # HEIMAN Water leakage sensor
    'HS1-WL-E': HS1WLE,                 # HEIMAN Water leakage sensor
    'HS2SK': HS2SK,                     # HEIMAN socket Zigbee (on/off, power measurement)
    'HS3SA': SmokeSensorAdapter,        # HEIMAN Smoke detector
    # Hive
    'HALIGHTDIMWWB22': DimmableBulbAdapter,     # Hive Active smart bulb white LED (B22)
    'HALIGHTDIMWWE27': DimmableBulbAdapter,     # Hive Active light dimmable
    '1613V': OnOffKwhAdapter,                   # Hive Active plug
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
    'LED1732G11': DimmableCtBulbAdapter,# IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, white spectrum, opal white
    'LED1733G7': DimmableCtBulbAdapter, # IKEA TRADFRI LED bulb E14 600 lumen, dimmable, white spectrum, opal white
    'LED1836G9': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb E26/E27 805 lumen, dimmable, opal white
    'LED1837R5': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb GU10 400 lumen, dimmable
    'LED1842G3': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb E27 250 lumen, dimmable, clear
    'ICPSHC24-10EU-IL-1': DimmableBulbAdapter,  # IKEA TRADFRI driver for wireless control (10 watt)
    'ICPSHC24-30EU-IL-1': DimmableBulbAdapter,  # IKEA TRADFRI driver for wireless control (30 watt)
    'ICTC-G-1': TradfriWirelessDimmer,  # IKEA TRADFRI wireless dimmer
    'L1527': DimmableCtBulbAdapter,     # IKEA FLOALT LED light panel, dimmable, white spectrum (30x30 cm)
    'L1528': DimmableCtBulbAdapter,     # IKEA FLOALT LED light panel, dimmable, white spectrum (30x90 cm)
    'L1529': DimmableCtBulbAdapter,     # IKEA FLOALT LED light panel, dimmable, white spectrum (60x60 cm)
    'L1531': DimmableCtBulbAdapter,     # IKEA SURTE door light panel, dimmable, white spectrum (38x64 cm)
    'E1524': TradfriRemoteControl,      # IKEA TRADFRI remote control
    'E1524/E1810': TradfriRemoteControl,      # IKEA TRADFRI remote control
    'E1525': MotionSensorAdapter,       # IKEA TRADFRI motion sensor
    'E1603': OnOffSwitchAdapter,        # IKEA TRADFRI control outlet
    'E1743': TradfriRemoteSwitchOnOff,        # IKEA TRADFRI ON/OFF switch
    'E1603/E1702': OnOffSwitchAdapter,  # IKEA TRADFRI control outlet
    'E1766': TradfriRemoteCloseOpen,    # IKEA TRADFRI open close remote
    'E1757': TradfriRollerBlind,        # IKEA TRADFRI roller blind
    # Immax
    'IM-Z3.0-DIM': DimmableBulbAdapter, # Immax LED E14/230V C35 5W TB 440LM ZIGBEE DIM
    # Innr
    'BY 165': DimmableBulbAdapter,      # Innr B22 Bulb dimmable
    'BY 185 C': RGBWAdapter,            # Innr B22 Bulb RGBW
    'BY 285 C': RGBWAdapter,            # Innr B22 Bulb RGBW
    'DL 110 N': DimmableBulbAdapter,    # Innr Spot narrow
    'DL 110 W': DimmableBulbAdapter,    # Innr Spot wide
    'PL 110': DimmableBulbAdapter,      # Innr Puck Light
    'RB 145': DimmableBulbAdapter,      # Innr E14 Candle
    'RB 165': DimmableBulbAdapter,      # Innr E27 Bulb
    'RB 175 W': DimmableBulbAdapter,    # Innr E27 Bulb warm dimming
    'RB 178 T': DimmableCtBulbAdapter,  # Innr Smart bulb tunable white E27
    'RB 185 C': RGBWAdapter,            # Innr E27 Bulb RGBW
    'RB 245': DimmableBulbAdapter,      # Innr E14 Candle
    'RB 248 T': DimmableCtBulbAdapter,  # Innr E14 Candle with white spectrum
    'RB 250 C': RGBWAdapter,            # Innr E14 Bulb RGBW
    'RB 265': DimmableBulbAdapter,      # Innr E27 Bulb
    'RB 278 T': DimmableBulbAdapter,    # Innr E27 Bulb
    'RB 285 C': RGBWAdapter,            # Innr E27 Bulb RGBW
    'RF 263': DimmableBulbAdapter,      # Innr E27 filament bulb dimmable
    'RF 265': DimmableBulbAdapter,      # Innr E27 bulb filament clea
    'RS 122': DimmableBulbAdapter,      # Innr GU10 Spot
    'RS 125': DimmableBulbAdapter,      # Innr GU10 Spot
    'RS 128 T': DimmableCtBulbAdapter,  # Innr GU10 Spot 350 lm, dimmable, white spectrum
    'RS 225': DimmableBulbAdapter,      # Innr GU10 Spot
    'RS 228 T': DimmableCtBulbAdapter,  # Innr GU10 Spot 350 lm
    'SL 110 M': DimmableBulbAdapter,    # Innr Spot Flex medium
    'SL 110 N': DimmableBulbAdapter,    # Innr Spot Flex narrow
    'SL 110 W': DimmableBulbAdapter,    # Innr Spot Flex wide
    'SP 120': InnrSP120Plug,            # Innr Smart plug
    'ST 110': DimmableBulbAdapter,      # Innr Strip Light
    'UC 110': DimmableBulbAdapter,      # Innr Under Cabinet Light
    # Iris
    '3210-L': OnOffSwitchAdapter,       # Iris Smart plug
    '3320-L': ContactAdapter,           # Iris Contact sensor
    '3326-L': MotionAndTemperatureSensorAdapter,    # Iris Motion and temperature sensor
    # JIAWEN
    'K2RGBW01': RGBWAdapter,            # JIAWEN Wireless Bulb E27 9W RGBW
    # Konke
    '2AJZ4KPKEY': KonkeButton,                      # Konke Multi-function button
    '2AJZ4KPFT': KonkeTemperatureHumiditySensor,    # Konke Temperature and humidity sensor
    # Ksentry
    'KS-SM001': OnOffSwitchAdapter,     # Ksentry Electronics Zigbee OnOff Controller
    # Lingan
    'DZ4743-00B': OnOffSwitchAdapter,   # Lingan Zigbee OnOff Controller
    # Livolo
    'TI0001': TI0001,                   # Livolo Switch TI0001
    # Müller Licht
    '404000/404005/404012': RGBWAdapter,            # Müller Licht Tint LED bulb GU10/E14/E27 350/470/806 lumen, dimmable, color, opal white
    '404006/404008/404004': DimmableCtBulbAdapter,  # Müller Licht Tint LED bulb GU10/E14/E27 350/470/806 lumen, dimmable, opal white
    # Nanoleaf
    'NL08-0800': DimmableBulbAdapter,   # Nanoleaf Ivy smart bulb
    # NET2GRID
    'N2G-SP': OnOffKwhAdapter,          # NET2GRID N2G-SP
    # Nue
    'FB56+ZSW05HG1.2': OnOffSwitchAdapter,      # Nue ZigBee one gang smart switch
    'HGZB-01A': DimmableBulbAdapter,    # Nue ZigBee smart light controller
    'HGZB-02A': DimmableBulbAdapter,    # Nue / 3A ZigBee smart light controller
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
    'AC03648': DimmableCtBulbAdapter,   # OSRAM SMART+ spot GU5.3 tunable white
    'AC08562': DimmableBulbAdapter,     # OSRAM SMART+ Candle E14 Dimmable White
    'AC01353010G': MotionAndTemperatureSensorAdapter,   # OSRAM SMART+ Motion Sensor
    'AC0251100NJ': DimmableBulbAdapter, # OSRAM SMART+ Switch Mini
    '4052899926110': RGBWAdapter,       # OSRAM Flex RGBW
    '4052899926158': DimmableBulbAdapter,   # OSRAM LIGHTIFY Surface Light TW
    '4058075036185': RGBWAdapter,       # OSRAM Outdoor Flex RGBW
    '4058075036147': RGBWAdapter,       # OSRAM Smart+ Gardenpole RGBW
    '4058075816718': RGBWAdapter,       # OSRAM SMART+ outdoor wall lantern RGBW
    '4058075816794': DimmableCtBulbAdapter, # OSRAM Smart+ Ceiling TW
    # Paul Neuhaus
    '100.424.11': DimmableCtBulbAdapter,    # Paul Neuhaus Q-INIGO LED ceiling light
    '100.110.39': RGBWAdapter,          # Paul Neuhaus Q-FLAG LED Panel, Smart-Home RGBW
    # Paulmann
    '50045': DimmableBulbAdapter,       # Paulmann SmartHome Zigbee LED-stripe
    '50049': RGBAdapter,                # Paulmann SmartHome Yourled RGB Controller
    # Philips
    '3216331P5': DimmableCtBulbAdapter, # Philips Hue white ambiance Aurelle Rectangle Panel Light
    '3216431P5': DimmableCtBulbAdapter, # Philips Hue white ambiance Aurelle round panel light
    '324131092621': HueDimmerSwitch,    # Philips Hue dimmer switch
    '3261030P7': DimmableCtBulbAdapter, # Philips Hue Being
    '3261331P7': DimmableCtBulbAdapter, # Philips Hue white ambiance Still
    '4033930P7': DimmableCtBulbAdapter, # Philips Hue white ambiance suspension Fair
    '4090130P7': RGBWAdapter,           # Philips Hue Sana
    '4090531P7': RGBWAdapter,           # Philips Hue Flourish white and color ambiance ceiling light
    '433714': DimmableBulbAdapter,      # Philips Hue Lux A19 bulb E27
    '464800': DimmableCtBulbAdapter,    # Philips Hue white ambiance BR30 flood light
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
    '9290018195': DimmableBulbAdapter,  # Philips Hue white GU10
    '9290019758': HueMotionSensor,      # Philips Hue motion outdoor sensor
    '1741830P7': RGBWAdapter,           # Philips Hue lily outdoor spotlight
    # ROBB
    'ROB_200-004-0': DimmableBulbAdapter,   # ROBB ZigBee AC phase-cut dimmer
    # Sengled
    'E1ACA4ABE38A': DimmableBulbAdapter,    # Sengled Element downlight smart LED bulb
    'E11-G13': DimmableBulbAdapter,         # Sengled Element Classic (A19)
    'E11-G23': DimmableBulbAdapter,         # Sengled Element Classic (A60)
    'E11-N1EA': RGBWAdapter,                # Sengled Element Plus Color (A19)
    'E12-N14': DimmableBulbAdapter,         # Sengled Element Classic (BR30)
    'Z01-A19NAE26': DimmableCtBulbAdapter,  # Sengled Element Plus (A19)
    'Z01-CIA19NAE26': DimmableBulbAdapter,  # Sengled Element Touch (A19)
    # Smart Home Pty
    'HGZB-07A': RGBWAdapter,            # Smart Home Pty RGBW Downlight
    'HGZB-20-DE': OnOffSwitchAdapter,   # Smart Home Pty Power plug
    # SmartThings
    'STSS-MULT-001': ContactAdapter,    # SmartThings Multipurpose sensor
    'F-MLT-US-2': ContactAdapter,       # SmartThings Multipurpose sensor (2016 model)
    'STS-PRS-251': SensorArrival,       # SmartThings SmartThings arrival sensor
    'STS-IRM-250': MotionAndTemperatureSensorAdapter,   # SmartThings Motion sensor (2016 model)
    '3305-S': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor (2014 model)
    '3325-S': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor (2015 model)
    'IM6001-MTP01': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor
    'IM6001-OTP05': OnOffSwitchAdapter, # SmartThings Outlet
    'IM6001-MPP01': ContactAdapter,     # SmartThings Multipurpose sensor (2018 model)
    '3300-S': SmartThingsDoorSensor,    # SmartThings Door sensor
    '3321-S': SmartThingsDoorSensor,    # SmartThings Multi Sensor (2015 model)
    # Stelpro
    'ST218': TemperatureSensorAdapter,  # Stelpro Built-in electronic thermostat
    # Sylvania
    '71831': DimmableCtBulbAdapter,     # Sylvania Smart Home adjustable white A19 LED bulb
    '72922-A': OnOffSwitchAdapter,      # Sylvania SMART+ Smart Plug
    '73693': RGBWAdapter,               # Sylvania LIGHTIFY LED RGBW A19
    '73739': RGBWAdapter,               # Sylvania LIGHTIFY LED RGBW BR30
    '73740': DimmableCtBulbAdapter,     # Sylvania LIGHTIFY LED adjustable white BR30
    '73742': DimmableCtBulbAdapter,     # Sylvania LIGHTIFY LED adjustable white RT 5/6
    '74282': DimmableCtBulbAdapter,     # Sylvania Smart Home adjustable white MR16 LED bulb
    '74283': DimmableBulbAdapter,       # Sylvania LIGHTIFY LED soft white dimmable A19
    '74696': DimmableBulbAdapter,       # Sylvania LIGHTIFY LED soft white dimmable A19
    'LTFY004': RGBAdapter,              # Sylvania LIGHTIFY LED gardenspot mini RGB
    # Swann One
    'SWO-KEF1PA': KEF1PA,				# Swann Key fob remote (panic, home, away, sleep)
    'SWO-WDS1PA': ContactAdapter,       # Swann Window/door sensor
    # Trust
    'ZLED-2709': DimmableBulbAdapter,   # Trust Smart Dimmable LED Bulb
    'ZPIR-8000': MotionSensorAdapter,   # Trust Motion Sensor
    'ZCTS-808': ContactAdapter,         # Trust Wireless contact sensor
    # Xiaomi
    'DJT11LM': SensorVibration,         # Xiaomi Aqara vibration sensor (drop, tilt and touch)
    'JTYJ-GD-01LM/BW': SmokeSensorAdapter,  # Xiaomi MiJia Honeywell smoke detector
    'JTQJ-BF-01LM/BW': JTQJBF01LM,      # Xiaomi MiJia gas leak detector
    'MCCGQ01LM': SensorMagnet,          # Xiaomi MiJia door & window contact sensor
    'MCCGQ11LM': SensorMagnet,          # Xiaomi Aqara door & window contact sensor
    'MFKZQ01LM': SensorCube,            # Xiaomi Mi smart home cube
    'QBCZ11LM': Plug,                   # Xiaomi Aqara socket Zigbee (on/off, power measurement)
    'QBKG03LM': AqaraDoubleWiredSwitch, # Xiaomi Aqara double key wired wall switch
    'QBKG04LM': OnOffSwitchAdapter,     # Xiaomi Aqara single key wired wall switch
    'QBKG11LM': Plug,                   # Xiaomi Aqara single key wired wall switch
    'QBKG12LM': AqaraDoubleWiredSwitch, # Xiaomi Aqara double key wired wall switch
    'RTCGQ01LM': MotionSensorAdapter,   # Xiaomi MiJia human body movement sensor
    'RTCGQ11LM': SensorMotionAq2,       # Xiaomi Aqara human body movement and illuminance sensor
    'SJCGQ11LM': WaterLeakSensorAdapter,# Xiaomi Aqara water leak sensor
    'WSDCGQ01LM': WSDCGQ01LM,           # Xiaomi MiJia temperature & humidity sensor
    'WSDCGQ11LM': WSDCGQ11LM,           # Xiaomi Aqara temperature, humidity and pressure sensor
    'WXKG01LM': WXKG01LM,               # Xiaomi MiJia wireless switch
    'WXKG02LM': WXKG02LM,               # Xiaomi Aqara double key wireless wall switch
    'WXKG03LM': WXKG03LM,               # Xiaomi Aqara single key wireless wall switch
    'WXKG11LM': WXKG11LM,               # Xiaomi Aqara wireless switch
    'WXKG12LM': WXKG12LM,               # Xiaomi Aqara wireless switch (with gyroscope)
    'ZNCZ02LM': ZNCZ02KM,               # Xiaomi Mi power plug ZigBee
    'ZNLDP12LM': DimmableCtBulbAdapter, # Xiaomi Aqara smart LED bulb
    'LLKZMK11LM':LLKZMK11LM,            # Xiaomi Aqara Two-way Control Module
    # iCasa
    'ICZB-IW11D': DimmableBulbAdapter,  # iCasa Zigbee 3.0 Dimmer
    # ilux
    '900008-WW': DimmableBulbAdapter,    # ilux Dimmable A60 E27 LED Bulb
    # Eurotronic
    'SPZB0001': ThermostatAdapter       # SPZB0001 thermostat
}
