from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.rgb_adapter import RGBAdapter
from adapters.rgbw_adapter import RGBWAdapter
from adapters.philips.hue_dimmer_switch import HueDimmerSwitch
from adapters.philips.hue_motion_sensor import HueMotionSensor


philips_adapters = {
    '046677476816': DimmableBulbAdapter,    # Philips Hue white PAR38 outdoor
    '046677552343': OnOffSwitchAdapter, # Philips Hue smart plug bluetooth
    '1741830P7': RGBWAdapter,           # Philips Hue Lily outdoor spot light
    '17436/30/P7': DimmableBulbAdapter, # Philips Hue Welcome white flood light
    '3115331PH': RGBWAdapter,           # Philips Phoenix light
    '3216131P5': DimmableCtBulbAdapter, # Philips Hue white ambiance Aurelle square panel light
    '3216231P5': DimmableCtBulbAdapter, # Philips Hue white ambiance Aurelle rectangle panel light
    '3216331P5': DimmableCtBulbAdapter, # Philips Hue white ambiance Aurelle Rectangle Panel Light
    '3216431P5': DimmableCtBulbAdapter, # Philips Hue white ambiance Aurelle round panel light
    '324131092621': HueDimmerSwitch,    # Philips Hue dimmer switch
    '3261030P7': DimmableCtBulbAdapter, # Philips Hue Being
    '3261331P7': DimmableCtBulbAdapter, # Philips Hue white ambiance Still
    '3306431P7': DimmableCtBulbAdapter, # Philips Hue Struana
    '4033930P7': DimmableCtBulbAdapter, # Philips Hue white ambiance suspension Fair
    '4090130P7': RGBWAdapter,           # Philips Hue Sana
    '4090531P7': RGBWAdapter,           # Philips Hue Flourish white and color ambiance ceiling light
    '4096730U7': DimmableCtBulbAdapter, # Philips Hue Cher ceiling light
    '433714': DimmableBulbAdapter,      # Philips Hue Lux A19 bulb E27
    '464800': DimmableCtBulbAdapter,    # Philips Hue white ambiance BR30 flood light
    '548727': RGBWAdapter,              # Philips Hue white and color ambiance BR30 with bluetooth
    '7099860PH': RGBAdapter,            # Philips LivingColors Aura
    '7146060PH': RGBWAdapter,           # Philips Hue Go
    '7199960PH': RGBAdapter,            # Philips Hue Iris
    '7299355PH': RGBAdapter,            # Philips Hue white and color ambiance LightStrip
    '7299760PH': RGBAdapter,            # Philips Hue Bloom
    '7602031P7': RGBWAdapter,           # Philips Hue Go with Bluetooth
    '8718696170625': DimmableBulbAdapter,   # Philips Hue Fuzo outdoor wall light
    '8718696449691': DimmableBulbAdapter,   # Philips Hue white Single bulb B22
    '8718696485880': RGBWAdapter,           # Philips Hue white and color ambiance GU10
    '8718696548738': DimmableCtBulbAdapter, # Philips Hue white ambiance E26/E27
    '8718696598283': DimmableCtBulbAdapter, # Philips Hue white ambiance GU10
    '8718696695203': DimmableCtBulbAdapter, # Philips Hue white ambiance E14
    '8718699673147': DimmableBulbAdapter,   # Philips Hue white A60 bulb E27 bluetooth
    '8718699688820': DimmableBulbAdapter,   # Philips Hue Filament Standard A60/E27 bluetooth
    '8718699688882': DimmableBulbAdapter,   # Philips Hue Fillament Bulb G93
    '915005106701': RGBWAdapter,        # Philips Hue white and color ambiance LightStrip plus
    '915005587401': DimmableCtBulbAdapter,  # Philips Hue white ambiance Adore light
    '915005733701': RGBWAdapter,        # Philips Hue white and color ambiance Play Lightbar
    '9290002579A': RGBWAdapter,         # Philips Hue white and color ambiance BR30
    '9290011370': DimmableBulbAdapter,  # Philips Hue white A60 bulb E27
    '9290011370B': DimmableBulbAdapter, # Philips Hue white A60 bulb E27
    '9290011998B': DimmableCtBulbAdapter,   # Philips Hue white ambiance E26
    '9290012573A': RGBWAdapter,         # Philips Hue white and color ambiance E26/E27 (with Color Temperature)
    '9290012607': HueMotionSensor,      # Philips Hue Motion Sensor (occupancy, temperature, illimination)
    '9290018187B': RGBWAdapter,         # Philips Hue white and color ambiance LightStrip outdoor
    '9290018195': DimmableBulbAdapter,  # Philips Hue white GU10
    '929001953101': RGBWAdapter,        # Philips Hue white and color ambiance GU10
    '929001953301': DimmableCtBulbAdapter,  # Philips Hue white ambiance GU10 with Bluetooth
    '9290019758': HueMotionSensor,      # Philips Hue motion outdoor sensor
    '9290020399': DimmableBulbAdapter,  # Philips Hue white E14
    '9290022166': RGBWAdapter,          # Philips Hue white and color ambiance E26/E27
    '9290022167': DimmableCtBulbAdapter,    # Philips Hue white ambiance E26 with Bluetooth
    '9290022169': DimmableCtBulbAdapter,    # Philips Hue white ambiance E27 with Bluetooth
    '929002240401': OnOffSwitchAdapter,     # Philips Hue smart plug - EU
    '929002241201': DimmableBulbAdapter,    # Philips Hue white filament Edison E27 LED
    '1741830P7': RGBWAdapter,           # Philips Hue lily outdoor spotlight
    'LWG004': DimmableBulbAdapter,      # Philips Hue white GU10 bluetooth
}