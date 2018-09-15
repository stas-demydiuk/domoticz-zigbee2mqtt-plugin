from adopters.adopter import SelectorSwitchAdopter

class Sensor86Sw2(SelectorSwitchAdopter):
    def __init__(self, devices):
        super().__init__(devices)
        self.level_names = ["Off", "left", "right", "both"]
        self.selector_type = self.SELECTOR_TYPE_BUTTONS

    def get_level_name(self, message):
        return message['click']