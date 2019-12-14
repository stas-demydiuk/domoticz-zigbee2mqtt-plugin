from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.rgb_adapter import RGBAdapter
from adapters.rgbw_adapter import RGBWAdapter
from adapters.philips.hue_dimmer_switch import HueDimmerSwitch
from adapters.philips.hue_motion_sensor import HueMotionSensor


philips_adapters = {
    '3216331P5': DimmableCtBulbAdapter, # Philips Hue white ambiance Aurelle Rectangle Panel Light
    '3216431P5': DimmableCtBulbAdapter, # Philips Hue white ambiance Aurelle round panel light
    '324131092621': HueDimmerSwitch,    # Philips Hue dimmer switch
    '3261030P7': DimmableCtBulbAdapter, # Philips Hue Being
    '3261331P7': DimmableCtBulbAdapter, # Philips Hue white ambiance Still
    '4033930P7': DimmableCtBulbAdapter, # Philips Hue white ambiance suspension Fair
    '4090130P7': RGBWAdapter,           # Philips Hue Sana
    '4090531P7': RGBWAdapter,           # Philips Hue Flourish white and color ambiance ceiling light
    '433714': DimmableBulbAdapter,      # Philips Hue Lux A19 bulb E27
    '464800': DimmableCtBulbAdapter,    # Philips Hue white ambiance BR30 flood light
    '7146060PH': RGBWAdapter,           # Philips Hue Go
    '7199960PH': RGBAdapter,            # Philips Hue Iris
    '7299355PH': RGBAdapter,            # Philips Hue white and color ambiance LightStrip
    '7299760PH': RGBAdapter,            # Philips Hue Bloom
    '8718696449691': DimmableBulbAdapter,   # Philips Hue white Single bulb B22
    '8718696485880': RGBWAdapter,           # Philips Hue white and color ambiance GU10
    '8718696548738': DimmableCtBulbAdapter, # Philips Hue white ambiance E26/E27
    '8718696598283': DimmableCtBulbAdapter, # Philips Hue white ambiance GU10
    '8718696695203': DimmableCtBulbAdapter, # Philips Hue white ambiance E14
    '8718699688882': DimmableBulbAdapter,   # Philips Hue Fillament Bulb G93
    '915005106701': RGBWAdapter,        # Philips Hue white and color ambiance LightStrip plus
    '915005733701': RGBWAdapter,        # Philips Hue white and color ambiance Play Lightbar
    '9290002579A': RGBWAdapter,         # Philips Hue white and color ambiance BR30
    '9290011370': DimmableBulbAdapter,  # Philips Hue white A60 bulb E27
    '9290012573A': RGBWAdapter,         # Philips Hue white and color ambiance E26/E27 (with Color Temperature)
    '9290012607': HueMotionSensor,      # Philips Hue Motion Sensor (occupancy, temperature, illimination)
    '9290018187B': RGBWAdapter,         # Philips Hue white and color ambiance LightStrip outdoor
    '9290018195': DimmableBulbAdapter,  # Philips Hue white GU10
    '9290019758': HueMotionSensor,      # Philips Hue motion outdoor sensor
    '1741830P7': RGBWAdapter,           # Philips Hue lily outdoor spotlight
}