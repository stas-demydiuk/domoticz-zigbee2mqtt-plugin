from adapters.philips.hue_dimmer_switch import HueDimmerSwitch
from adapters.philips.hue_motion_sensor import HueMotionSensor


philips_adapters = {
    '324131092621': HueDimmerSwitch,        # Philips Hue dimmer switch
    '9290012607': HueMotionSensor,          # Philips Hue Motion Sensor (occupancy, temperature, illimination)
    '9290019758': HueMotionSensor,          # Philips Hue motion outdoor sensor
}