from adapters.bitron.AV201032 import AV201032
from adapters.bitron.siren import BitronSirenAdapterWithBattery

bitron_adapters = {
    'AV2010/32': AV201032,                     # Bitron Wireless wall thermostat with relay
    '902010/29': BitronSirenAdapterWithBattery,# Bitron Outdoor siren
    'AV2010/29': BitronSirenAdapterWithBattery # Bitron Outdoor siren
}
