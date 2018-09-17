from adapters.selector_switch import SelectorSwitchAdopter

class SensorSwitch(SelectorSwitchAdopter):
    def __init__(self, devices):
        super().__init__(devices)
        self.level_names = ['Off', 'Click', 'Double Click', 'Triple Click', 'Quadruple Click', 'Many clicks', 'Long Click', 'Long Click Release']
        self.selector_type = self.SELECTOR_TYPE_MENU

    def get_level_name(self, message):
        actions = ['single', 'double', 'triple', 'quadruple', 'many' 'long', 'long_release']

        if ('click' not in message.raw):
            return 'Off'

        action = message.raw['click']
        action_index = actions.index(action)
        
        return self.level_names[action_index + 1]