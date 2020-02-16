from adapters.contact_adapter import ContactAdapter
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.generic.motion_temp_sensor import MotionAndTemperatureSensorAdapter
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
    'IM6001-OTP05': OnOffSwitchAdapter, # SmartThings Outlet
    'IM6001-MPP01': ContactAdapter,     # SmartThings Multipurpose sensor (2018 model)
    '3300-S': SmartThingsDoorSensor,    # SmartThings Door sensor
    '3321-S': SmartThingsDoorSensor,    # SmartThings Multi Sensor (2015 model)
    'STS-OUT-US-2': OnOffSwitchAdapter, # SmartThings Outlet
    'F-APP-UK-V2': OnOffSwitchAdapter,  # SmartThings Outlet
}