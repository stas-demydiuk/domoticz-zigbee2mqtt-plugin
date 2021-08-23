import domoticz
from devices.device import Device


class OnOffLight(Device):
    def __init__(self, alias, device_name_suffix=' (Light)'):
        super().__init__(alias, 'light', device_name_suffix)
        self.icon = 1

    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Switch", Image=self.icon)

    def set_state_feature(self, feature):
        self.state_feature = feature

    def set_icon(self, icon_number):
        self.icon = icon_number

    def get_message_value(self, message):
        return message.raw

    def get_state_value(self, value):
        state_value_key = self.state_feature['property']
        
        if state_value_key in value:
            return value[state_value_key].lower()
        else:
            return None

    def get_numeric_value(self, value, device):
        state_value = self.get_state_value(value)

        if (state_value == 'on'):
            return 1
        elif (state_value == 'off'):
            return 0
        else:
            return device.nValue

    def get_string_value(self, value, device):
        n_value = self.get_numeric_value(value, device)
        return 'On' if n_value == 1 else 'Off'

    def generate_command(self, command, level, color):
        cmd = command.upper()
        state_value_key = self.state_feature['property']

        if cmd == 'ON':
            return {
                state_value_key: self.state_feature['value_on']
            }
        elif cmd == 'OFF':
            return {
                state_value_key: self.state_feature['value_off']
            }
