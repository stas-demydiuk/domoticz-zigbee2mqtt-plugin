from adapters.generic.siren import SirenAdapter
from adapters.samsung.sensor_arrival import SensorArrival


samsung_adapters = {
    'STS-PRS-251': SensorArrival,       # SmartThings SmartThings arrival sensor
    'SZ-SRN12N': SirenAdapter,          # SmartThings Smart siren
}