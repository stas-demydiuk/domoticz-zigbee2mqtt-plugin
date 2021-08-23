import domoticz
from devices.switch.on_off_switch import OnOffSwitch


class SirenSwitch(OnOffSwitch):
    def __init__(self, devices, alias, value_key, device_name_suffix=''):
        super().__init__(devices, alias, value_key, device_name_suffix)

    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, Type=244, Subtype=73, Switchtype=4)
