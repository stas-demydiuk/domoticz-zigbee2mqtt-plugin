from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class HueDimmerSwitch(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'dimmer', 'action')
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
        self.devices.append(self.switch)
        
    def convert_message(self, message):
        message = super().convert_message(message)
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