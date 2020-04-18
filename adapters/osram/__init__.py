from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.rgbw_adapter import RGBWAdapter
from adapters.generic.motion_temp_sensor import MotionAndTemperatureSensorAdapter
from adapters.osram.smart_mini_switch import SmartMiniSwitch


osram_adapters = {
    '4052899926110': RGBWAdapter,       # OSRAM Flex RGBW
    '4052899926158': DimmableBulbAdapter,   # OSRAM LIGHTIFY Surface Light TW
    '4058075036147': RGBWAdapter,       # OSRAM Smart+ Gardenpole RGBW
    '4058075036185': RGBWAdapter,       # OSRAM Outdoor Flex RGBW
    '4058075047853': RGBWAdapter,       # OSRAM Smart+ gardenpole 4W RGBW
    '4058075816718': RGBWAdapter,       # OSRAM SMART+ outdoor wall lantern RGBW
    '4058075816732': RGBWAdapter,       # OSRAM SMART+ outdoor lantern RGBW
    '4058075816794': DimmableCtBulbAdapter, # OSRAM Smart+ Ceiling TW
    '595UGR22': DimmableCtBulbAdapter,  # OSRAM OSRAM LED panel TW 595 UGR22
    'AA68199': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY LED PAR16 50 GU10 tunable white
    'AA69697': RGBWAdapter,             # OSRAM Classic A60 RGBW
    'AA70155': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY LED A19 tunable white / Classic A60 TW
    'AB3257001NJ': OnOffSwitchAdapter,  # OSRAM Smart+ plug
    'AB32840': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY LED Classic B40 tunable white
    'AB35996': RGBWAdapter,             # OSRAM Smart+ Spot GU10 Multicolor
    'AB401130055': DimmableCtBulbAdapter,   # OSRAM LIGHTIFY Surface Light LED Tunable White
    'AC01353010G': MotionAndTemperatureSensorAdapter,   # OSRAM SMART+ Motion Sensor
    'AC0251100NJ': SmartMiniSwitch,     # OSRAM SMART+ Switch Mini
    'AC0251100NJ/AC0251700NJ': SmartMiniSwitch, # OSRAM SMART+ Switch Mini
    'AC0363900NJ': RGBWAdapter,         # OSRAM Smart+ mini gardenpole RGBW
    'AC03641': DimmableBulbAdapter,     # OSRAM LIGHTIFY LED Classic A60 clear
    'AC03642': DimmableCtBulbAdapter,   # OSRAM SMART+ CLASSIC A 60 TW
    'AC03645': RGBWAdapter,             # OSRAM LIGHTIFY LED CLA60 E27 RGBW
    'AC03647': RGBWAdapter,             # OSRAM SMART+ LED CLASSIC E27 RGBW
    'AC03648': DimmableCtBulbAdapter,   # OSRAM SMART+ spot GU5.3 tunable white
    'AC08559': RGBWAdapter,             # OSRAM SMART+ Spot GU10 Multicolor
    'AC08560': DimmableBulbAdapter,     # OSRAM SMART+ LED PAR16 GU10
    'AC08562': DimmableBulbAdapter,     # OSRAM SMART+ Candle E14 Dimmable White
    'AC10691': OnOffSwitchAdapter,      # OSRAM Smart+ plug
    'AC10786-DIM': DimmableBulbAdapter, # OSRAM SMART+ classic E27 dimmable
    'AC10787': DimmableCtBulbAdapter,   # OSRAM SMART+ classic E27 TW
    'ST8AU-CON': DimmableBulbAdapter,   # OSRAM OSRAM SubstiTUBE T8 Advanced UO Connected
}