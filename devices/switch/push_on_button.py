import Domoticz
from devices.device import Device


class PushOnButton(Device):
    def create_device(self, unit, device_id, device_name, message):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=244, subtype=73, Switchtype=9).Create()

    def get_numeric_value(self, value, device):
        return 1 if value.lower() == 'on' else 0

    def get_string_value(self, value, device):
        return 'On' if value.lower() == 'on' else 'Off'
