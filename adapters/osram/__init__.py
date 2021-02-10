from adapters.generic.motion_temp_sensor import MotionAndTemperatureSensorAdapter
from adapters.osram.smart_mini_switch import SmartMiniSwitch


osram_adapters = {
    'AC01353010G': MotionAndTemperatureSensorAdapter,   # OSRAM SMART+ Motion Sensor
    'AC0251100NJ': SmartMiniSwitch,                     # OSRAM SMART+ Switch Mini
    'AC0251100NJ/AC0251700NJ': SmartMiniSwitch,         # OSRAM SMART+ Switch Mini
}