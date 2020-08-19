from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.rgbw_adapter import RGBWAdapter
from adapters.gledopto.GLC0082ID import GLC0082ID


gledopto_adapters = {
    'GD-CZ-006': DimmableBulbAdapter,   # Gledopto Zigbee LED Driver
    'GL-B-001Z': RGBWAdapter,           # Gledopto Smart 4W E14 RGB / CCT LED bulb
    'GL-B-007Z': RGBWAdapter,           # Gledopto Smart 6W E27 RGB / CW LED bulb
    'GL-B-008Z': RGBWAdapter,           # Gledopto Smart 12W E27 RGB / CW LED bulb
    'GL-B-008ZS': RGBWAdapter,          # Gledopto Smart 12W E27 RGB / CW LED bulb
    'GL-C-006': DimmableCtBulbAdapter,  # Gledopto Zigbee LED controller WW/CW Dimmer
    'GL-C-007': RGBWAdapter,            # Gledopto Zigbee LED controller RGBW
    'GL-C-007S': RGBWAdapter,           # Gledopto Zigbee LED controller RGBW plus model    
    'GL-C-007-1ID': RGBWAdapter,        # Gledopto Zigbee LED controller RGBW (1 ID)
    'GL-C-007-2ID': RGBWAdapter,        # Gledopto Zigbee LED controller RGBW plus model (2 ID)
    'GL-C-007/GL-C-008': RGBWAdapter,   # Gledopto Zigbee LED controller RGB + CCT or RGBW
    'GL-C-008': RGBWAdapter,            # Gledopto Zigbee LED controller RGB + CCT / RGBW / WWCW / Dimmer
    'GL-C-008-1ID': RGBWAdapter,        # Gledopto Zigbee LED controller RGB + CCT (1 ID)
    'GL-C-008-2ID': GLC0082ID,          # Zigbee LED controller RGB + CCT (2 ID)
    'GL-C-008S': RGBWAdapter,           # Gledopto Zigbee LED controller RGB + CCT plus model
    'GL-C-009': DimmableBulbAdapter,    # Gledopto Zigbee LED controller dimmer
    'GL-D-003Z': RGBWAdapter,           # Gledopto LED RGB + CCT downlight
    'GL-FL-004TZ': RGBWAdapter,         # Gledopto Zigbee 10W floodlight RGB CCT
    'GL-MC-001': RGBWAdapter,           # Gledopto Zigbee USB mini LED controller RGB + CCT
    'GL-S-003Z': RGBWAdapter,           # Gledopto Smart RGBW GU10
    'GL-S-004Z': DimmableCtBulbAdapter, # Gledopto Smart Wnite GU10
    'GL-S-007Z': RGBWAdapter,           # Gledopto Smart RGBW GU10
    'GL-S-007ZS': RGBWAdapter,          # Gledopto Smart RGB+CCT GU10
    'GL-S-008Z': RGBWAdapter,           # Gledopto Soposh dual white and color
    'GL-W-001Z': OnOffSwitchAdapter,    # Gledopto Zigbee ON/OFF Wall Switch
}
