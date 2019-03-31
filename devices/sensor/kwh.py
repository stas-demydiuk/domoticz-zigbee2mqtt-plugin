import Domoticz
from devices.device import Device


class KwhSensor(Device):
    def __init__(self, devices, alias, value_key, device_name_suffix=''):
        super().__init__(devices, alias, ';'.join(value_key), device_name_suffix)
        self.value_keys = value_key
    
    def create_device(self, unit, device_id, device_name):
        options = {}
        options['EnergyMeterMode'] = '1'

        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="kWh", Options=options).Create()

    def get_message_value(self, message):
        value = {}

        for item in self.value_keys:
            if item in message.raw:
                value[item] = message.raw[item]

        return value if len(value) > 0 else None

    def get_numeric_value(self, value, device):
        return 0

    def get_string_value(self, value, device):
        if 'energy' in value:
            return str(value['power']) + ";" + str(value['energy'] * 1000)
        else:
            return str(value['power'])
