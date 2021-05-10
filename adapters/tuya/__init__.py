from adapters.tuya.TS0002 import TS0002
from adapters.tuya.TS0012 import TS0012
from adapters.tuya.TS0013 import TS0013
from adapters.tuya.TS0015 import TS0015
from adapters.tuya.TS0601 import TS0601


tuya_adapters = {
    'TS0002': TS0002,                           # TuYa 2 gang switch
    'TS0012': TS0012,                           # TuYa Smart light switch - 2 gang without neutral wire
    'TS0013': TS0013,                           # TuYa Smart light switch - 3 gang without neutral wire
    'TS0015': TS0015,                           # TuYa Multiprise with 4 AC outlets and 2 USB super charging ports (10A or 16A)
    'TS0601_thermostat': TS0601,                # TuYa Radiator valve with thermostat
}
