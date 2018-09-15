from adopters.adopter import SelectorSwitchAdopter

class AqaraCube(SelectorSwitchAdopter):
    def __init__(self, devices):
        super().__init__(devices)
        self.level_names = ["Off", "flip90", "flip180", "tap", "shake", "fall", "rotate_left", "rotate_right", "slide"]