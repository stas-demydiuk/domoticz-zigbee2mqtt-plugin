import Domoticz
from adapters import adapter_by_model

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

    def _register_device(self, domoticz_devices, device_data):
        model = device_data['model']
        Domoticz.Log('Device ' + model + ' ' + device_data['ieee_addr'] + ' (' + device_data['friendly_name'] + ')')

        self.devices[device_data['ieee_addr']] = device_data
        
        if model in adapter_by_model:
            adapter = adapter_by_model[model](domoticz_devices)
            adapter.register(device_data)

    def clear(self):
        self.devices = {}

    def update(self, domoticz_devices, zigbee_devices):
        for item in zigbee_devices:
            if 'type' in item and item['type'] == 'Coordinator':
                Domoticz.Debug('Coordinator address is ' + item['ieeeAddr'])
                continue

            friendly_name = item['friendly_name'] if 'friendly_name' in item else item['ieeeAddr']

            if 'model' in item:
                device_data = {
                    'type': item['type'],
                    'model': item['model'],
                    'ieee_addr': item['ieeeAddr'],
                    'friendly_name': friendly_name
                }

                self._register_device(domoticz_devices, device_data)
            else:
                Domoticz.Log('Device ' + item['ieeeAddr'] + ' (' + friendly_name + ') doesn\'t have "model" attribute, skipped')

    def get_device_by_id(self, ieee_addr):
        return self.devices[ieee_addr] if ieee_addr in self.devices else None

    def get_device_by_name(self, friendly_name):
        for key, device in self.devices.items():
            if (device['friendly_name'] == friendly_name):
                return device
