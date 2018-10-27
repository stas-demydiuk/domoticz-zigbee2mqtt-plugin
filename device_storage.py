import Domoticz


class DeviceStorage:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        if DeviceStorage.__instance == None:
            DeviceStorage()

        return DeviceStorage.__instance 

    def __init__(self):
        if DeviceStorage.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DeviceStorage.__instance = self
            self.devices = {}

    def update(self, devices):
        for item in devices:
            self.devices[item['ieeeAddr']] = {
                'type': item['type'],
                'model': item['model'],
                'ieee_addr': item['ieeeAddr'],
                'friendly_name': item['friendly_name']
            }

            Domoticz.Debug('Device ' + item['model'] + ' ' + item['ieeeAddr'] + ' (' + item['friendly_name'] + ')')

    def get_device_by_id(self, ieee_addr):
        return self.devices[ieee_addr] if ieee_addr in self.devices else None

    def get_device_by_name(self, friendly_name):
        for key, device in self.devices.items():
            if (device['friendly_name'] == friendly_name):
                return device