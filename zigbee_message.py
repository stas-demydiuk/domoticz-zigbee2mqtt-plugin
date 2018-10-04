class ZigbeeMessage:
    def __init__(self, message):
        self.raw = message

    def has_device_info(self):
        return 'device' in self.raw

    def get_device_ieee_addr(self):
        return self.raw['device']['ieeeAddr']

    def get_device_name(self):
        return self.raw['device']['friendlyName']

    def get_device_model(self):
        return self.raw['device']['modelId']

    def get_signal_level(self):
        if ('linkquality' in self.raw):
            return int(int(self.raw['linkquality']) * 100 / 255)
        else:
            return None

    def get_battery_level(self):
        power_source = self.raw['device']['powerSource']

        if (power_source == 'Battery'):
            if ('battery' in self.raw):
                return int(float(self.raw['battery']))
            else:
                return None
        else:
            return 255
