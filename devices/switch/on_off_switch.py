import Domoticz
from devices.device import Device


class OnOffSwitch(Device):
    def __init__(self, devices, alias, value_key, device_name_suffix=''):
        super().__init__(devices, alias, value_key, device_name_suffix)
        self.icon = 1

    def set_icon(self, icon_number):
        self.icon = icon_number

    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Switch", Image=self.icon).Create()

    def get_numeric_value(self, value, device):
        if (value.lower() == 'on'):
            return 1
        elif (value.lower() == 'off'):
            return 0
        else:
            return device.nValue

    def get_string_value(self, value, device):
        n_value = self.get_numeric_value(value, device)
        return 'On' if n_value == 1 else 'Off'

    def handle_command(self, device_data, command, level, color):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)

        Domoticz.Debug('Command "' + command + '" from device "' + device.Name + '"')

        self.update_device(device, {
            'nValue': self.get_numeric_value(command, device),
            'sValue': self.get_string_value(command, device)
        })
