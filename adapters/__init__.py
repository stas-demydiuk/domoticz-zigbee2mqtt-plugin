from adapters.base_adapter import Adapter
from adapters.contact_adapter import ContactAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.rgb_adapter import RGBAdapter
from adapters.rgbw_adapter import RGBWAdapter
from adapters.weiser_lock import WeiserLock
from adapters.bitron import bitron_adapters
from adapters.cr import cr_adapters
from adapters.ewelink import ewelink_adapters
from adapters.feibit import feibit_adapters
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.generic.motion_temp_sensor import MotionAndTemperatureSensorAdapter
from adapters.generic.on_off_kwh import OnOffKwhAdapter
from adapters.generic.smoke_sensor import SmokeSensorAdapter
from adapters.generic.temperature_sensor import TemperatureSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.generic.thermostat import ThermostatAdapter
from adapters.generic.water_leak_sensor import WaterLeakSensorAdapter
from adapters.gira.light_link import GiraLightLink
from adapters.gledopto import gledopto_adapters
from adapters.heiman import heiman_adapters
from adapters.icasa import icasa_adapters
from adapters.ikea import ikea_adapters
from adapters.immax import immax_adapters
from adapters.innr import innr_adapters
from adapters.konke import konke_adapters
from adapters.life_control import life_control_adapters
from adapters.livolo.TI0001 import TI0001
from adapters.lumi import lumi_adapters
from adapters.meazon.dinrail import DinrailAdapter
from adapters.neo import neo_adapters
from adapters.netvox.Z809A import NetvoxZ809A
from adapters.osram import osram_adapters
from adapters.oujiabao.CR701_YZ import CR701_YZ
from adapters.siterwell.GS361AH04 import GS361AH04
from adapters.samsung import samsung_adapters
from adapters.schneider_electric import schneider_adapters
from adapters.sinope import sinope_adapters
from adapters.sonoff import sonoff_adapters
from adapters.philips import philips_adapters
from adapters.swo.KEF1PA import KEF1PA
from adapters.trust import trust_adapters
from adapters.tuya import tuya_adapters
from adapters.tuya.TS0002 import TS0002
from adapters.tuyatec import tuyatec_adapters
from adapters.diy.ptvo_switch import PtvoSwitch
from adapters.diy.zigup import ZigupAdapter
from adapters.zemismart import zemismart_adapters

adapter_by_model = dict({
    # Alecto Smart Home
    'RH3001': ContactAdapter,                   # Alecto Smart Home - Smart sensor door / window
    'RH3052': TemperatureHumiditySensorAdapter,   # Alecto Smart Home branded Smart sensor temp and humidity / TUYATEC - TT001ZAV20 temp and humidity sensor
    # AduroSmart
    '81809': RGBWAdapter,               # AduroSmart ERIA colors and white shades smart light bulb A19
    # Airam
    '4713407': DimmableBulbAdapter,     # Airam LED OP A60 ZB 9W/827 E27
    # Anchor
    '67200BL': OnOffSwitchAdapter,      # Anchor Vetaar smart plug
    # Belkin
    'F7C033': DimmableBulbAdapter,      # Belkin WeMo smart LED bulb
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
    'ZigUP': ZigupAdapter,              # Custom devices (DiY) ZigUP
    'DIYRuZ_magnet': ContactAdapter,    # DIYRuZ DIYRuZ_magnet
    # Dresden Elektronik
    'Mega23M12': RGBWAdapter,           # Dresden Elektronik ZigBee Light Link wireless electronic ballast
    'XVV-Mega23M12': DimmableCtBulbAdapter, # Dresden Elektronik ZigBee Light Link wireless electronic ballast color temperature
    # EcoSmart
    'D1531': DimmableBulbAdapter,       # EcoSmart A19 bright white bulb
    'D1532': DimmableBulbAdapter,       # EcoSmart A19 soft white bulb (on/off, brightness)
    'D1821': RGBWAdapter,               # EcoSmart A19 RGB bulb (on/off, brightness, color temperature, color xy)
    # Essentials
    '120112': GS361AH04,                # Essentials Smart home heizkörperthermostat premium (white-label of Siterwell GS361A-H04) 
    # Eurotronic
    'SPZB0001': ThermostatAdapter,      # SPZB0001 thermostat
    # ELKO
    '316GLEDRF': DimmableBulbAdapter,   # Elko ESH RS16 316GLED dimmer RF PH. ZigBee in-wall smart dimmer. (on/off, brightness)
    # GE
    '22670': DimmableBulbAdapter,       # GE Link smart LED light bulb, BR30 soft white (2700K)
    '45852GE': DimmableBulbAdapter,     # GE ZigBee plug-in smart dimmer
    '45853GE': OnOffSwitchAdapter,      # GE ZigBee plug-in smart switch
    '45856GE': OnOffSwitchAdapter,      # GE ZigBee in-wall smart switch
    '45857GE': DimmableBulbAdapter,     # GE ZigBee in-wall smart dimmer
    # Gira
    '2430-100': GiraLightLink,          # Gira ZigBee Light Link wall transmitter
    # Hive
    'HALIGHTDIMWWB22': DimmableBulbAdapter,     # Hive Active smart bulb white LED (B22)
    'HALIGHTDIMWWE27': DimmableBulbAdapter,     # Hive Active light dimmable
    '1613V': OnOffKwhAdapter,                   # Hive Active plug
    # ITEAD
    'BASICZBR3': OnOffSwitchAdapter,    # ITEAD SONOFF ZigBee DIY Smart Switch
    # Iris
    '3210-L': OnOffSwitchAdapter,       # Iris Smart plug
    '3320-L': ContactAdapter,           # Iris Contact sensor
    '3326-L': MotionAndTemperatureSensorAdapter,    # Iris Motion and temperature sensor
    # JIAWEN
    'K2RGBW01': RGBWAdapter,            # JIAWEN Wireless Bulb E27 9W RGBW
    # Ksentry
    'KS-SM001': OnOffSwitchAdapter,     # Ksentry Electronics Zigbee OnOff Controller
    # Lingan
    'DZ4743-00B': OnOffSwitchAdapter,   # Lingan Zigbee OnOff Controller
    # Livolo
    'TI0001': TI0001,                   # Livolo Switch TI0001
    # Lonhonso
    'X702': TS0002,                     # Lonhonso 2 gang switch
    # Meazon
    'MEAZON_DINRAIL': DinrailAdapter,   # Meazon DinRail 1-phase meter
    # Müller Licht
    '404000/404005/404012': RGBWAdapter,            # Müller Licht Tint LED bulb GU10/E14/E27 350/470/806 lumen, dimmable, color, opal white
    '404006/404008/404004': DimmableCtBulbAdapter,  # Müller Licht Tint LED bulb GU10/E14/E27 350/470/806 lumen, dimmable, opal white
    '404021': OnOffSwitchAdapter,                   # Müller Licht Tint smart switch
    # Nanoleaf
    'NL08-0800': DimmableBulbAdapter,   # Nanoleaf Ivy smart bulb
    # Netvox
    'Z809A': NetvoxZ809A,               # Netvox Power socket with power consumption monitoring
    # NET2GRID
    'N2G-SP': OnOffKwhAdapter,          # NET2GRID N2G-SP
    # Nue
    'FB56+ZSW05HG1.2': OnOffSwitchAdapter,      # Nue ZigBee one gang smart switch
    'HGZB-01A': OnOffSwitchAdapter,     # Nue ZigBee smart light controller
    'HGZB-02A': DimmableBulbAdapter,    # Nue / 3A ZigBee smart light controller
    # Oujiabao
    'CR701_YZ': CR701_YZ,               # Oujiabao Gas and carbon monoxide alarm
    # Paul Neuhaus
    '100.424.11': DimmableCtBulbAdapter,    # Paul Neuhaus Q-INIGO LED ceiling light
    '100.110.39': RGBWAdapter,          # Paul Neuhaus Q-FLAG LED Panel, Smart-Home RGBW
    # Paulmann
    '50045': DimmableBulbAdapter,       # Paulmann SmartHome Zigbee LED-stripe
    '50049': RGBAdapter,                # Paulmann SmartHome Yourled RGB Controller
    # ROBB
    'ROB_200-003-0': OnOffSwitchAdapter,    # ROBB Zigbee AC in wall switch
    'ROB_200-004-0': DimmableBulbAdapter,   # ROBB ZigBee AC phase-cut dimmer
    'ROB_200-014-0': DimmableBulbAdapter,   # ROBB ZigBee AC phase-cut rotary dimmer
    # Salus
    'SP600': OnOffKwhAdapter,               # Salus Smart plug
    # Sengled
    'E1ACA4ABE38A': DimmableBulbAdapter,    # Sengled Element downlight smart LED bulb
    'E11-G13': DimmableBulbAdapter,         # Sengled Element Classic (A19)
    'E11-G23': DimmableBulbAdapter,         # Sengled Element Classic (A60)
    'E11-N1EA': RGBWAdapter,                # Sengled Element Plus Color (A19)
    'E12-N14': DimmableBulbAdapter,         # Sengled Element Classic (BR30)
    'Z01-A19NAE26': DimmableCtBulbAdapter,  # Sengled Element Plus (A19)
    'Z01-CIA19NAE26': DimmableBulbAdapter,  # Sengled Element Touch (A19)
    # Shenzhen Homa
    'HLD812-Z-SC': DimmableBulbAdapter, # Shenzhen Homa Smart LED driver
    'HLC610-Z': DimmableBulbAdapter,    # Shenzhen Homa Wireless dimmable controller
    'HLC821-Z-SC': DimmableBulbAdapter, # Shenzhen Homa ZigBee AC phase-cut dimmer
    # Siterwell
    'GS361A-H04': GS361AH04,            # Siterwell Radiator valve with thermostat
    # Smart Home Pty
    'HGZB-07A': RGBWAdapter,            # Smart Home Pty RGBW Downlight
    'HGZB-20-DE': OnOffSwitchAdapter,   # Smart Home Pty Power plug
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
    'SWO-MOS1PA': MotionSensorAdapter,  # Swann Motion and temperature sensor
    # Weiser
    '9GED18000-009': WeiserLock,        # Weiser SmartCode 10
    '9GED21500-005': WeiserLock,        # Weiser SmartCode 10 Touch
    # ilux
    '900008-WW': DimmableBulbAdapter,   # ilux Dimmable A60 E27 LED Bulb
    # Unbranded DIY adapters
    'ptvo.switch': PtvoSwitch           # cc2530 zigbee module with pvto.switch firmware (buttons only for now!)
},
    **bitron_adapters,
    **cr_adapters,
    **ewelink_adapters,
    **feibit_adapters,
    **gledopto_adapters,
    **heiman_adapters,
    **icasa_adapters,
    **ikea_adapters,
    **immax_adapters,
    **innr_adapters,
    **konke_adapters,
    **life_control_adapters,
    **lumi_adapters,
    **neo_adapters,
    **osram_adapters,
    **philips_adapters,
    **samsung_adapters,
    **schneider_adapters,
    **sinope_adapters,
    **sonoff_adapters,
    **trust_adapters,
    **tuya_adapters,
    **tuyatec_adapters,
    **zemismart_adapters,
)
