from adapters.rgbw_adapter import RGBWAdapter
from adapters.generic.motion_temp_sensor import MotionAndTemperatureSensorAdapter
from adapters.osram.smart_mini_switch import SmartMiniSwitch


osram_adapters = {
    '4052899926110': RGBWAdapter,       # OSRAM Flex RGBW
    '4058075036147': RGBWAdapter,       # OSRAM Smart+ Gardenpole RGBW
    '4058075036185': RGBWAdapter,       # OSRAM Outdoor Flex RGBW
    '4058075047853': RGBWAdapter,       # OSRAM Smart+ gardenpole 4W RGBW
    '4058075816718': RGBWAdapter,       # OSRAM SMART+ outdoor wall lantern RGBW
    '4058075816732': RGBWAdapter,       # OSRAM SMART+ outdoor lantern RGBW
    'AA69697': RGBWAdapter,             # OSRAM Classic A60 RGBW
    'AB35996': RGBWAdapter,             # OSRAM Smart+ Spot GU10 Multicolor
    'AC01353010G': MotionAndTemperatureSensorAdapter,   # OSRAM SMART+ Motion Sensor
    'AC0251100NJ': SmartMiniSwitch,     # OSRAM SMART+ Switch Mini
    'AC0251100NJ/AC0251700NJ': SmartMiniSwitch, # OSRAM SMART+ Switch Mini
    'AC0363900NJ': RGBWAdapter,         # OSRAM Smart+ mini gardenpole RGBW
    'AC03645': RGBWAdapter,             # OSRAM LIGHTIFY LED CLA60 E27 RGBW
    'AC03647': RGBWAdapter,             # OSRAM SMART+ LED CLASSIC E27 RGBW
    'AC08559': RGBWAdapter,             # OSRAM SMART+ Spot GU10 Multicolor
}