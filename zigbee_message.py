class ZigbeeMessage:
    def __init__(self, message):
        self.raw = message

    def get_device_ieee_addr(self):
        return self.raw['device']['ieeeAddr']

    def get_device_name(self):
        return self.raw['device']['friendlyName']

    def get_signal_level(self):
        return int(int(self.raw['linkquality']) * 100 / 255)

    def get_battery_level(self):
        power_source = self.raw['device']['powerSource']

        if (power_source == 'Battery'):
            if ('battery' in self.raw):
                return int(float(self.raw['battery']))
            else:
                return None
        else:
            return 255