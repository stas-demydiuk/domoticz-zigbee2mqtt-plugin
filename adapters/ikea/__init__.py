from adapters.base_adapter import Adapter
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.rgb_adapter import RGBAdapter
from adapters.generic.blind_adapter import BlindAdapter
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.ikea.symfonisk import Symfonisk
from adapters.ikea.tradfri_remote_control import TradfriRemoteControl
from adapters.ikea.tradfri_wireless_dimmer import TradfriWirelessDimmer
from adapters.ikea.tradfri_switch_on_off import TradfriRemoteSwitchOnOff
from adapters.ikea.tradfri_remote_close_open import TradfriRemoteCloseOpen


ikea_adapters = {
    'LED1536G5': DimmableCtBulbAdapter, # IKEA TRADFRI LED bulb E12/E14 400 lumen, dimmable, white spectrum, opal white
    'LED1537R6': DimmableCtBulbAdapter, # IKEA TRADFRI LED bulb GU10 400 lumen, dimmable, white spectrum
    'LED1537R6/LED1739R5': DimmableCtBulbAdapter, # IKEA TRADFRI LED bulb GU10 400 lumen, dimmable, white spectrum
    'LED1545G12': DimmableCtBulbAdapter,# IKEA TRADFRI LED bulb E26/E27 980 lumen, dimmable, white spectrum, opal white
    'LED1546G12': DimmableCtBulbAdapter,# IKEA TRADFRI LED bulb E26/E27 950 lumen, dimmable, white spectrum, clear
    'LED1622G12': DimmableBulbAdapter,  # IKEA TRADFRI LED bulb E26 1000 lumen, dimmable, opal white
    'LED1623G12': DimmableBulbAdapter,  # IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, opal white
    'LED1624G9': RGBAdapter,            # IKEA TRADFRI LED bulb E27 600 lumen, dimmable, color, opal white
    'LED1649C5': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb E14 400 lumen, dimmable warm white, chandelier opal
    'LED1650R5': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb GU10 400 lumen, dimmable
    'LED1732G11': DimmableCtBulbAdapter,# IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, white spectrum, opal white
    'LED1733G7': DimmableCtBulbAdapter, # IKEA TRADFRI LED bulb E14 600 lumen, dimmable, white spectrum, opal white
    'LED1736G9': DimmableCtBulbAdapter, # IKEA TRADFRI LED bulb E27 806 lumen, dimmable, white spectrum, clear
    'LED1738G7': DimmableCtBulbAdapter, # IKEA TRADFRI LED bulb E12 600 lumen, dimmable, white spectrum, opal white
    'LED1836G9': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb E26/E27 805 lumen, dimmable, opal white
    'LED1837R5': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb GU10 400 lumen, dimmable
    'LED1836G9': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb E26/E27 806 lumen, dimmable, warm white
    'LED1842G3': DimmableBulbAdapter,   # IKEA TRADFRI LED bulb E27 250 lumen, dimmable, clear
    'LED1903C5': DimmableCtBulbAdapter, # IKEA TRADFRI LED bulb E14 470 lumen, dimmable, white spectrum, opal white
    'LED1903C5/LED1835C6': DimmableCtBulbAdapter,   # IKEA TRADFRI LED bulb E14 470 lumen, dimmable, white spectrum, opal white
    'ICPSHC24-10EU-IL-1': DimmableBulbAdapter,  # IKEA TRADFRI driver for wireless control (10 watt)
    'ICPSHC24-30EU-IL-1': DimmableBulbAdapter,  # IKEA TRADFRI driver for wireless control (30 watt)
    'ICTC-G-1': TradfriWirelessDimmer,  # IKEA TRADFRI wireless dimmer
    'L1527': DimmableCtBulbAdapter,     # IKEA FLOALT LED light panel, dimmable, white spectrum (30x30 cm)
    'L1528': DimmableCtBulbAdapter,     # IKEA FLOALT LED light panel, dimmable, white spectrum (30x90 cm)
    'L1529': DimmableCtBulbAdapter,     # IKEA FLOALT LED light panel, dimmable, white spectrum (60x60 cm)
    'L1531': DimmableCtBulbAdapter,     # IKEA SURTE door light panel, dimmable, white spectrum (38x64 cm)
    'T1820': DimmableCtBulbAdapter,     # IKEA LEPTITER Recessed spot light
    'T1828': DimmableCtBulbAdapter,     # IKEA GUNNARP panel round
    'T1829': DimmableCtBulbAdapter,     # IKEA GUNNARP LED light panel, dimmable, white spectrum (40x40 cm)
    'E1524': TradfriRemoteControl,      # IKEA TRADFRI remote control
    'E1524/E1810': TradfriRemoteControl,# IKEA TRADFRI remote control
    'E1525': MotionSensorAdapter,       # IKEA TRADFRI motion sensor
    'E1525/E1745': MotionSensorAdapter, # IKEA TRADFRI motion sensor
    'E1603': OnOffSwitchAdapter,        # IKEA TRADFRI control outlet
    'E1743': TradfriRemoteSwitchOnOff,  # IKEA TRADFRI ON/OFF switch
    'E1744': Symfonisk,                 # IKEA SYMFONISK sound controller
    'E1746': Adapter,                   # IKEA TRADFRI signal repeater
    'E1603/E1702': OnOffSwitchAdapter,  # IKEA TRADFRI control outlet
    'E1766': TradfriRemoteCloseOpen,    # IKEA TRADFRI open close remote
    'E1757': BlindAdapter,              # IKEA TRADFRI roller blind
    'E1926': BlindAdapter,              # IKEA TRADFRI roller blind
}