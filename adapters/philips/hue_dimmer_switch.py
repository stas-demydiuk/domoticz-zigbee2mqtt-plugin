from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch
from devices.switch.dimmer_switch import DimmerSwitch


class HueDimmerSwitch(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch('dimmer', 'action')
        self.switch.add_level('off-press', 'off-press')
        self.switch.add_level('off-press-double', 'off-press-double')
        self.switch.add_level('off-press-triple', 'off-press-triple')
        self.switch.add_level('off-hold', 'off-hold')
        self.switch.add_level('off-hold-release', 'off-hold-release')
        self.switch.add_level('down-press', 'down-press')
        self.switch.add_level('down-press-double', 'down-press-double')
        self.switch.add_level('down-press-triple', 'down-press-triple')
        self.switch.add_level('down-hold', 'down-hold')
        self.switch.add_level('down-hold-release', 'down-hold-release')
        self.switch.add_level('up-press', 'up-press')
        self.switch.add_level('up-press-double', 'up-press-double')
        self.switch.add_level('up-press-triple', 'up-press-triple')
        self.switch.add_level('up-hold', 'up-hold')
        self.switch.add_level('up-hold-release', 'up-hold-release')
        self.switch.add_level('on-press', 'on-press')
        self.switch.add_level('on-press-double', 'on-press-double')
        self.switch.add_level('on-press-triple', 'on-press-triple')
        self.switch.add_level('on-hold', 'on-hold')
        self.switch.add_level('on-hold-release', 'on-hold-release')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.switch.disable_value_check_on_update()
        self.devices.append(self.switch)
        # Add dimmer
        self.dimmer = DimmerSwitch('bright', 'brightness')
        self.devices.append(self.dimmer)
        
    def convert_message(self, message):
        message = super().convert_message(message)
        if 'action' in message.raw and 'counter' in message.raw:
            simpleaction = str(message.raw['action'])
            if simpleaction.endswith('press'):
                if message.raw['counter'] == 2:
                    addstring = '-double'
                elif message.raw['counter'] == 3:
                    addstring = '-triple'
                else:
                    addstring = ''
                message.raw['action'] = message.raw['action'] + addstring

        return message
