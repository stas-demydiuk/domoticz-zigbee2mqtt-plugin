import domoticz
from devices.device import Device


class KwhSensor(Device):
    def __init__(self, alias, value_key, device_name_suffix=''):
        super().__init__(alias, ';'.join(value_key), device_name_suffix)
        self.value_keys = value_key
        self.energy_multiplier = 1000
    
    def create_device(self, unit, device_id, device_name):
        options = {}
        options['EnergyMeterMode'] = '0' if len(self.value_keys) == 2 else '1'

        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="kWh", Options=options)

    def get_message_value(self, message):
        value = []

        for item in self.value_keys:
            if item not in message.raw:
                return None
            
            value.append(message.raw[item])

        return value if len(value) > 0 else None

    def get_numeric_value(self, value, device):
        return 0

    def get_string_value(self, value, device):
        if len(value) == 2:
            return str(value[0]) + ";" + str(int(value[1] * self.energy_multiplier))
        else:
            return str(value[0])
