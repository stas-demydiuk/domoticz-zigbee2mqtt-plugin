from adapters.contact_adapter import ContactAdapter
from adapters.generic.motion_temp_sensor import MotionAndTemperatureSensorAdapter
from adapters.generic.on_off_kwh import OnOffKwhAdapter
from adapters.generic.siren import SirenAdapter
from adapters.samsung.sensor_arrival import SensorArrival
from adapters.samsung.sensor_door import SmartThingsDoorSensor


samsung_adapters = {
    'STSS-MULT-001': ContactAdapter,    # SmartThings Multipurpose sensor
    'F-MLT-US-2': ContactAdapter,       # SmartThings Multipurpose sensor (2016 model)
    'STS-PRS-251': SensorArrival,       # SmartThings SmartThings arrival sensor
    'STS-IRM-250': MotionAndTemperatureSensorAdapter,   # SmartThings Motion sensor (2016 model)
    '3305-S': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor (2014 model)
    '3325-S': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor (2015 model)
    'IM6001-MTP01': MotionAndTemperatureSensorAdapter, # SmartThings Motion sensor
    'IM6001-MPP01': ContactAdapter,     # SmartThings Multipurpose sensor (2018 model)
    '3300-S': SmartThingsDoorSensor,    # SmartThings Door sensor
    '3321-S': SmartThingsDoorSensor,    # SmartThings Multi Sensor (2015 model)
    'STS-OUT-US-2': OnOffKwhAdapter,    # SmartThings Zigbee smart plug with power meter
    'GP-WOU019BBDWG': OnOffKwhAdapter,  # SmartThings Outlet with power meter
    'F-APP-UK-V2': OnOffKwhAdapter,     # SmartThings Zigbee Outlet UK with power meter
    'SZ-SRN12N': SirenAdapter,          # SmartThings Smart siren
}