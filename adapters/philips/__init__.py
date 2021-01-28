from adapters.rgbw_adapter import RGBWAdapter
from adapters.philips.hue_dimmer_switch import HueDimmerSwitch
from adapters.philips.hue_motion_sensor import HueMotionSensor


philips_adapters = {
    '1741830P7': RGBWAdapter,               # Philips Hue Lily outdoor spot light
    '1741830P7': RGBWAdapter,               # Philips Hue lily outdoor spotlight
    '1742930P7': RGBWAdapter,               # Philips Hue outdoor Impress wall lamp
    '1743030P7': RGBWAdapter,               # Philips Hue outdoor Impress wall lamp
    '1743130P7': RGBWAdapter,               # Philips Hue Impress outdoor Pedestal
    '1743230P7': RGBWAdapter,               # Philips Hue outdoor Impress lantern
    '1744130P7': RGBWAdapter,               # Philips Hue Econic outdoor Pedestal
    '1746130P7': RGBWAdapter,               # Philips Hue Attract
    '3115331PH': RGBWAdapter,               # Philips Phoenix light
    '324131092621': HueDimmerSwitch,        # Philips Hue dimmer switch
    '4080148P9': RGBWAdapter,               # Philips Hue Signe table light
    '4080248P9': RGBWAdapter,               # Philips Hue Signe floor light
    '4090130P7': RGBWAdapter,               # Philips Hue Sana
    '4090331P9': RGBWAdapter,               # Philips Hue Ensis
    '4090531P7': RGBWAdapter,               # Philips Hue Flourish white and color ambiance ceiling light
    '4090631P7': RGBWAdapter,               # Philips Hue Flourish white and color ambiance pendant light
    '5045148P7': RGBWAdapter,               # Philips Hue Centura
    '5062131P7': RGBWAdapter,               # Philips Hue white and color ambience Argenta spot (1 spot)
    '5062231P7': RGBWAdapter,               # Philips Hue white and color ambience Argenta spot (2 spots)
    '5062331P7': RGBWAdapter,               # Philips Hue white and color ambience Argenta spot (3 spots)
    '5062431P7': RGBWAdapter,               # Philips Hue white and color ambience Argenta spot (4 spots)
    '548727': RGBWAdapter,                  # Philips Hue white and color ambiance BR30 with bluetooth
    '5900131C5': RGBWAdapter,               # Philips Hue Aphelion downlight
    '7121131PU': RGBWAdapter,               # Philips Hue Beyond white and color ambiance suspension light
    '7146060PH': RGBWAdapter,               # Philips Hue Go
    '7602031P7': RGBWAdapter,               # Philips Hue Go with Bluetooth
    '8718696167991': RGBWAdapter,           # Philips Hue Calla outdoor
    '8718696170557': RGBWAdapter,           # Philips Hue Calla outdoor
    '8718696485880': RGBWAdapter,           # Philips Hue white and color ambiance GU10
    '915005106701': RGBWAdapter,            # Philips Hue white and color ambiance LightStrip plus
    '915005733701': RGBWAdapter,            # Philips Hue white and color ambiance Play Lightbar
    '9290002579A': RGBWAdapter,             # Philips Hue white and color ambiance BR30
    '9290012573A': RGBWAdapter,             # Philips Hue white and color ambiance E26/E27 (with Color Temperature)
    '9290012607': HueMotionSensor,          # Philips Hue Motion Sensor (occupancy, temperature, illimination)
    '9290018187B': RGBWAdapter,             # Philips Hue white and color ambiance LightStrip outdoor
    '929001953101': RGBWAdapter,            # Philips Hue white and color ambiance GU10
    '9290019758': HueMotionSensor,          # Philips Hue motion outdoor sensor
    '9290022166': RGBWAdapter,              # Philips Hue white and color ambiance E26/E27
    '9290022891': RGBWAdapter,              # Philips Hue outdoor led strip
}