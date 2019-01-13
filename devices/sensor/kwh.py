import Domoticz
from devices.device import Device


class KwhSensor(Device):
    def create_device(self, unit, device_id, device_name):
        options = {}
        options['EnergyMeterMode'] = '1'

        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="kWh", Options=options).Create()

    def get_numeric_value(self, value, device):
        return 0

    def get_string_value(self, value, device):
        return str(value)
