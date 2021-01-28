from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
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
    '3216131P5': DimmableCtBulbAdapter,     # Philips Hue white ambiance Aurelle square panel light
    '3216231P5': DimmableCtBulbAdapter,     # Philips Hue white ambiance Aurelle rectangle panel light
    '3216331P5': DimmableCtBulbAdapter,     # Philips Hue white ambiance Aurelle Rectangle Panel Light
    '3216431P5': DimmableCtBulbAdapter,     # Philips Hue white ambiance Aurelle round panel light
    '324131092621': HueDimmerSwitch,        # Philips Hue dimmer switch
    '3261030P7': DimmableCtBulbAdapter,     # Philips Hue Being
    '3261331P7': DimmableCtBulbAdapter,     # Philips Hue white ambiance Still
    '3306431P7': DimmableCtBulbAdapter,     # Philips Hue Struana
    '3402831P7': DimmableCtBulbAdapter,     # Philips Hue white ambiance bathroom mirror light Adore
    '3435011P7': DimmableCtBulbAdapter,     # Philips Hue white ambiance bathroom ceiling light Adore
    '4023330P7': DimmableCtBulbAdapter,     # Philips Hue white ambiance suspension Amaze
    '4033930P7': DimmableCtBulbAdapter,     # Philips Hue white ambiance suspension Fair
    '4034031P7': DimmableCtBulbAdapter,     # Philips Hue Fair
    '4080148P9': RGBWAdapter,               # Philips Hue Signe table light
    '4080248P9': RGBWAdapter,               # Philips Hue Signe floor light
    '4090130P7': RGBWAdapter,               # Philips Hue Sana
    '4090331P9': RGBWAdapter,               # Philips Hue Ensis
    '4090531P7': RGBWAdapter,               # Philips Hue Flourish white and color ambiance ceiling light
    '4090631P7': RGBWAdapter,               # Philips Hue Flourish white and color ambiance pendant light
    '4096730U7': DimmableCtBulbAdapter,     # Philips Hue Cher ceiling light
    '4098430P7': DimmableCtBulbAdapter,     # Philips Hue Being Pendant
    '4503848C5': DimmableCtBulbAdapter,     # Philips Hue white ambiance Muscari pendant light
    '464800': DimmableCtBulbAdapter,        # Philips Hue white ambiance BR30 flood light
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
    '8718696548738': DimmableCtBulbAdapter, # Philips Hue white ambiance E26/E27
    '8718696598283': DimmableCtBulbAdapter, # Philips Hue white ambiance GU10
    '8718696695203': DimmableCtBulbAdapter, # Philips Hue white ambiance E14
    '915005106701': RGBWAdapter,            # Philips Hue white and color ambiance LightStrip plus
    '915005587401': DimmableCtBulbAdapter,  # Philips Hue white ambiance Adore light
    '915005733701': RGBWAdapter,            # Philips Hue white and color ambiance Play Lightbar
    '9290002579A': RGBWAdapter,             # Philips Hue white and color ambiance BR30
    '9290011998B': DimmableCtBulbAdapter,   # Philips Hue white ambiance E26
    '9290012573A': RGBWAdapter,             # Philips Hue white and color ambiance E26/E27 (with Color Temperature)
    '9290012607': HueMotionSensor,          # Philips Hue Motion Sensor (occupancy, temperature, illimination)
    '9290018187B': RGBWAdapter,             # Philips Hue white and color ambiance LightStrip outdoor
    '929001953101': RGBWAdapter,            # Philips Hue white and color ambiance GU10
    '929001953301': DimmableCtBulbAdapter,  # Philips Hue white ambiance GU10 with Bluetooth
    '9290019758': HueMotionSensor,          # Philips Hue motion outdoor sensor
    '9290022166': RGBWAdapter,              # Philips Hue white and color ambiance E26/E27
    '9290022167': DimmableCtBulbAdapter,    # Philips Hue white ambiance E26 with Bluetooth
    '9290022169': DimmableCtBulbAdapter,    # Philips Hue white ambiance E27 with Bluetooth
    '9290022891': RGBWAdapter,              # Philips Hue outdoor led strip
}