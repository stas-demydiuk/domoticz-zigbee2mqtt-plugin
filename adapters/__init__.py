from adapters.base_adapter import Adapter
from adapters.weiser_lock import WeiserLock
from adapters.bitron import bitron_adapters
from adapters.ewelink import ewelink_adapters
from adapters.feibit import feibit_adapters
from adapters.generic.motion_temp_sensor import MotionAndTemperatureSensorAdapter
from adapters.generic.on_off_kwh import OnOffKwhAdapter
from adapters.generic.plug import PlugAdapter
from adapters.generic.temperature_sensor import TemperatureSensorAdapter
from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from adapters.generic.thermostat import ThermostatAdapter
from adapters.gira.light_link import GiraLightLink
from adapters.gledopto import gledopto_adapters
from adapters.heiman import heiman_adapters
from adapters.icasa import icasa_adapters
from adapters.ikea import ikea_adapters
from adapters.innr import innr_adapters
from adapters.konke import konke_adapters
from adapters.life_control import life_control_adapters
from adapters.livolo.TI0001 import TI0001
from adapters.lumi import lumi_adapters
from adapters.meazon.dinrail import DinrailAdapter
from adapters.neo import neo_adapters
from adapters.osram import osram_adapters
from adapters.oujiabao.CR701_YZ import CR701_YZ
from adapters.siterwell.GS361AH04 import GS361AH04
from adapters.samsung import samsung_adapters
from adapters.schneider_electric import schneider_adapters
from adapters.sinope import sinope_adapters
from adapters.sonoff import sonoff_adapters
from adapters.philips import philips_adapters
from adapters.trust import trust_adapters
from adapters.tuya import tuya_adapters
from adapters.tuya.TS0002 import TS0002
from adapters.tuyatec import tuyatec_adapters
from adapters.diy.ptvo_switch import PtvoSwitch
from adapters.diy.zigup import ZigupAdapter
from adapters.zemismart import zemismart_adapters
from adapters.diy.diyruzrt import DIYRuZ_RT

adapter_by_model = dict({
    # Alecto Smart Home
    'RH3052': TemperatureHumiditySensorAdapter,   # Alecto Smart Home branded Smart sensor temp and humidity / TUYATEC - TT001ZAV20 temp and humidity sensor
    # Bosch
    'RADON TriTech ZB': MotionAndTemperatureSensorAdapter,  # Bosch Wireless motion detector
    'ISW-ZPR1-WP13': MotionAndTemperatureSensorAdapter,     # Bosch Motion sensor
    # Custom devices (DiY)
    'CC2530.ROUTER': Adapter,           # Zigbee router based on CC2530 chip
    'ZigUP': ZigupAdapter,              # Custom devices (DiY) ZigUP
    'DIYRuZ_RT': DIYRuZ_RT,             # DIYRuZ_RT SonoffBasic ZBR2+DS18b20
    # Essentials
    '120112': GS361AH04,                # Essentials Smart home heizkörperthermostat premium (white-label of Siterwell GS361A-H04) 
    # Eurotronic
    'SPZB0001': ThermostatAdapter,      # SPZB0001 thermostat
    # Gira
    '2430-100': GiraLightLink,          # Gira ZigBee Light Link wall transmitter
    # Hive
    '1613V': OnOffKwhAdapter,                   # Hive Active plug
    # Iris
    '3326-L': MotionAndTemperatureSensorAdapter,    # Iris Motion and temperature sensor
    # Livolo
    'TI0001': TI0001,                   # Livolo Switch TI0001
    # Lonhonso
    'X702': TS0002,                     # Lonhonso 2 gang switch
    # Meazon
    'MEAZON_DINRAIL': DinrailAdapter,   # Meazon DinRail 1-phase meter
    # Netvox
    'Z809A': PlugAdapter,               # Netvox Power socket with power consumption monitoring
    # NET2GRID
    'N2G-SP': OnOffKwhAdapter,          # NET2GRID N2G-SP
    # Oujiabao
    'CR701_YZ': CR701_YZ,               # Oujiabao Gas and carbon monoxide alarm
    # Salus
    'SP600': OnOffKwhAdapter,               # Salus Smart plug
    # Siterwell
    'GS361A-H04': GS361AH04,            # Siterwell Radiator valve with thermostat
    # Stelpro
    'ST218': TemperatureSensorAdapter,  # Stelpro Built-in electronic thermostat
    # Weiser
    '9GED18000-009': WeiserLock,        # Weiser SmartCode 10
    '9GED21500-005': WeiserLock,        # Weiser SmartCode 10 Touch
    # Unbranded DIY adapters
    'ptvo.switch': PtvoSwitch           # cc2530 zigbee module with pvto.switch firmware (buttons only for now!)
},
    **bitron_adapters,
    **ewelink_adapters,
    **feibit_adapters,
    **gledopto_adapters,
    **heiman_adapters,
    **icasa_adapters,
    **ikea_adapters,
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
