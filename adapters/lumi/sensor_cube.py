from adapters.selector_switch import SelectorSwitchAdopter

class SensorCube(SelectorSwitchAdopter):
    def __init__(self, devices):
        super().__init__(devices)
        self.level_names = ["Off", "flip90", "flip180", "tap", "shake", "fall", "rotate_left", "rotate_right", "slide"]
        self.selector_style = self.SELECTOR_TYPE_MENU

    def get_level_name(self, message):
        return message.raw['action'] if 'action' in message.raw else 'Off'