from adapters.base_adapter import Adapter
from adapters.ikea.symfonisk import Symfonisk
from adapters.ikea.tradfri_remote_control import TradfriRemoteControl
from adapters.ikea.tradfri_wireless_dimmer import TradfriWirelessDimmer
from adapters.ikea.tradfri_switch_on_off import TradfriRemoteSwitchOnOff
from adapters.ikea.styrbar_remote_control import StyrbarRemoteControl


ikea_adapters = {
    'ICTC-G-1': TradfriWirelessDimmer,  # IKEA TRADFRI wireless dimmer
    'E1524': TradfriRemoteControl,      # IKEA TRADFRI remote control
    'E1524/E1810': TradfriRemoteControl,# IKEA TRADFRI remote control
    'E1743': TradfriRemoteSwitchOnOff,  # IKEA TRADFRI ON/OFF switch
    'E1744': Symfonisk,                 # IKEA SYMFONISK sound controller
    'E1746': Adapter,                   # IKEA TRADFRI signal repeater
    'E2001/E2002': StyrbarRemoteControl,# IKEA STYRBAR remote control
}
