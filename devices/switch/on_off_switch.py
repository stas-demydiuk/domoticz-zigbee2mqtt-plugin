import Domoticz
from devices.device import Device


class OnOffSwitch(Device):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Switch", Image=1).Create()

    def get_numeric_value(self, value, device):
        return 1 if value.lower() == 'on' else 0

    def get_string_value(self, value, device):
        return 'On' if value.lower() == 'on' else 'Off'

    def update_device(self, device, values):
        if values['nValue'] != device.nValue or values['sValue'] != device.sValue:
            super().update_device(device, values)

    def handle_command(self, device_data, command, level, color):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)

        Domoticz.Debug('Command "' + command + '" from device "' + device.Name + '"')

        self.update_device(device, {
            'nValue': self.get_numeric_value(command, device),
            'sValue': self.get_string_value(command, device)
        })