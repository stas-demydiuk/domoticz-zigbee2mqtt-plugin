from adapters.generic.siren import SirenAdapterWithBattery
from adapters.heiman.HS1CAE import HS1CAE
from adapters.heiman.HS1RC import HeimanAlarmRemoteAdapter


heiman_adapters = {
    'HS1CA-E': HS1CAE,                  # HEIMAN Monoxyde detector
    'HS1CA-M': HS1CAE,                  # HEIMAN Monoxyde detector
    'HS2WD-E': SirenAdapterWithBattery, # HEIMAN Smart siren
	'HS1RC-EM': HeimanAlarmRemoteAdapter, # HEIMAN Alarm remote
}
