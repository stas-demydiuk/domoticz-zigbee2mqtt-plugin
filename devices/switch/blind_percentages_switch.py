import Domoticz
from devices.device import Device


class BlindSwitch(Device):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=244, Subtype=73, Switchtype=13).Create()

    def set_state_feature(self, feature):
        self.state_feature = feature

    def set_position_feature(self, feature):
        self.position_feature = feature

    def get_numeric_value(self, value, device):
        if value == self.position_feature['value_max']:
            return 0
        elif value == self.position_feature['value_min']:
            return 1
        else:
            return 2

    def get_string_value(self, value, device):
        return str(int(100-value))

    def generate_command(self, command, level, color):
        cmd = command.upper()
        state_value_key = self.state_feature['property']
        position_value_key = self.position_feature['property']

        if cmd == 'ON':
            return {
                state_value_key: self.state_feature['value_on']
            }
        elif cmd == 'OFF':
            return {
                state_value_key: self.state_feature['value_off']
            }
        elif cmd == 'SET LEVEL':
            return {
                position_value_key: int(100 - level)
            }
        elif cmd == 'STOP':
            return {
                state_value_key: 'stop'
            }
        else:
            Domoticz.Error('Blind switch: unable to handle command "' + command + '"')
        
