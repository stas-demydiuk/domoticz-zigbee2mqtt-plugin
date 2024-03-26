from adapters.base_adapter import Adapter
from adapters.onesti import onesti_adapters
from adapters.weiser_lock import WeiserLock
from adapters.bitron import bitron_adapters
from adapters.ecodim import ecodim_adapters
from adapters.feibit import feibit_adapters
from adapters.generic.thermostat import ThermostatAdapter
from adapters.gledopto import gledopto_adapters
from adapters.heiman import heiman_adapters
from adapters.icasa import icasa_adapters
from adapters.ikea import ikea_adapters
from adapters.life_control import life_control_adapters
from adapters.lumi import lumi_adapters
from adapters.meazon.dinrail import DinrailAdapter
from adapters.moes import moes_adapters
from adapters.neo import neo_adapters
from adapters.osram import osram_adapters
from adapters.oujiabao.CR701_YZ import CR701_YZ
from adapters.siterwell.GS361AH04 import GS361AH04
from adapters.samsung import samsung_adapters
from adapters.schneider_electric import schneider_adapters
from adapters.sinope import sinope_adapters
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
    # Custom devices (DiY)
    'CC2530.ROUTER': Adapter,           # Zigbee router based on CC2530 chip
    'ZigUP': ZigupAdapter,              # Custom devices (DiY) ZigUP
    'DIYRuZ_RT': DIYRuZ_RT,             # DIYRuZ_RT SonoffBasic ZBR2+DS18b20
    # Essentials
    '120112': GS361AH04,                # Essentials Smart home heizkörperthermostat premium (white-label of Siterwell GS361A-H04) 
    # Eurotronic
    'SPZB0001': ThermostatAdapter,      # SPZB0001 thermostat
    # Lonhonso
    'X702': TS0002,                     # Lonhonso 2 gang switch
    # Meazon
    'MEAZON_DINRAIL': DinrailAdapter,   # Meazon DinRail 1-phase meter
    # Oujiabao
    'CR701_YZ': CR701_YZ,               # Oujiabao Gas and carbon monoxide alarm
    # Siterwell
    'GS361A-H04': GS361AH04,            # Siterwell Radiator valve with thermostat
    # Weiser
    '9GED18000-009': WeiserLock,        # Weiser SmartCode 10
    '9GED21500-005': WeiserLock,        # Weiser SmartCode 10 Touch
    # Unbranded DIY adapters
    'ptvo.switch': PtvoSwitch           # cc2530 zigbee module with pvto.switch firmware (buttons only for now!)
},
    **bitron_adapters,
    **ecodim_adapters,
    **feibit_adapters,
    **gledopto_adapters,
    **heiman_adapters,
    **icasa_adapters,
    **ikea_adapters,
    **life_control_adapters,
    **lumi_adapters,
    **moes_adapters,
    **neo_adapters,
    **osram_adapters,
    **philips_adapters,
    **samsung_adapters,
    **schneider_adapters,
    **sinope_adapters,
    **trust_adapters,
    **tuya_adapters,
    **tuyatec_adapters,
    **zemismart_adapters,
    **onesti_adapters,
)
