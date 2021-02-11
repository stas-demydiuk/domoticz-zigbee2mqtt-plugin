from adapters.generic.motion_temp_sensor import MotionAndTemperatureSensorAdapter
from adapters.generic.on_off_kwh import OnOffKwhAdapter
from adapters.generic.siren import SirenAdapter
from adapters.samsung.sensor_arrival import SensorArrival


samsung_adapters = {
    'STS-PRS-251': SensorArrival,       # SmartThings SmartThings arrival sensor
    'STS-IRM-250': MotionAndTemperatureSensorAdapter,   # SmartThings Motion sensor (2016 model)
    '3305-S': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor (2014 model)
    '3325-S': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor (2015 model)
    'IM6001-MTP01': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor
    'STS-OUT-US-2': OnOffKwhAdapter,    # SmartThings Zigbee smart plug with power meter
    'GP-WOU019BBDWG': OnOffKwhAdapter,  # SmartThings Outlet with power meter
    'F-APP-UK-V2': OnOffKwhAdapter,     # SmartThings Zigbee Outlet UK with power meter
    'SZ-SRN12N': SirenAdapter,          # SmartThings Smart siren
}