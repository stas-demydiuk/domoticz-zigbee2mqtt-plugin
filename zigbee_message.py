class ZigbeeMessage:
    def __init__(self, message):
        self.raw = message

    def get_signal_level(self):
        if ('linkquality' in self.raw):
            return int(int(self.raw['linkquality']) * 11 / 255)
        else:
            return None

    def get_battery_level(self):
        if ('battery' in self.raw):
            return int(float(self.raw['battery']))
        else:
            return None
