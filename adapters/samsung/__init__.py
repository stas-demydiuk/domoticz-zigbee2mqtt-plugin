from adapters.generic.motion_temp_sensor import MotionAndTemperatureSensorAdapter
from adapters.generic.siren import SirenAdapter
from adapters.samsung.sensor_arrival import SensorArrival


samsung_adapters = {
    'STS-PRS-251': SensorArrival,       # SmartThings SmartThings arrival sensor
    'STS-IRM-250': MotionAndTemperatureSensorAdapter,   # SmartThings Motion sensor (2016 model)
    '3305-S': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor (2014 model)
    '3325-S': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor (2015 model)
    'IM6001-MTP01': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor
    'SZ-SRN12N': SirenAdapter,          # SmartThings Smart siren
}