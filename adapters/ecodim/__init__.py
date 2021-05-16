from adapters.base_adapter import Adapter
from adapters.ecodim.zigbee2buttonwallswitch import Zigbee2ButtonWallSwitch


ecodim_adapters = {
    'ED-10011': Zigbee2ButtonWallSwitch,  # EcoDim Zigbee 2 button wall switch - black
}
