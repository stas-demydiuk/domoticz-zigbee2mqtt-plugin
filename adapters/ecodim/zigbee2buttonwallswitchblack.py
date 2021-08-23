from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.dimmer_switch import DimmerSwitch
from devices.switch.selector_switch import SelectorSwitch

class Zigbee2ButtonWallSwitchBlack(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(DimmerSwitch('dimmer', 'brightness'))

        self.switch = SelectorSwitch('switch', 'action')
        self.switch.add_level('Off', 'off')
        self.switch.add_level('On', 'on')
        self.switch.add_level('Up', 'brightness_move_up')
        self.switch.add_level('Down', 'brightness_move_down')
        self.switch.add_level('Stop', 'brightness_stop')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.switch.disable_value_check_on_update()

        self.devices.append(self.switch)
