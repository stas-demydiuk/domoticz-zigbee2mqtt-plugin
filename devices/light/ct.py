import json
import Domoticz
from devices.light.dimmer import DimmerLight


class CTLight(DimmerLight):
    MAX_CT_VALUE = 255

    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=241, Subtype=8, Switchtype=7).Create()

    def set_color_temp_feature(self, feature):
        self.color_temp_feature = feature

    # Returns color temperature in 0..255 range
    def get_color_value(self, value, device):
        value_key = self.color_temp_feature['property']
        value_min = self.color_temp_feature['value_min']
        value_max = self.color_temp_feature['value_max']
        
        if value_key in value:
            return json.dumps({
                'm': 2,  # ColorModeTemp
                't': int((value[value_key] - value_min) * self.MAX_CT_VALUE / (value_max - value_min))
            })
        else:
            return device.Color

    def get_device_args(self, value, device, message):
        args = super().get_device_args(value, device, message)

        return dict(args, Color=self.get_color_value(value, device))

    def generate_command(self, command, level, color):
        cmd = command.upper()

        if cmd == 'SET COLOR':
            state_value_key = self.state_feature['property']
            value_key = self.color_temp_feature['property']
            value_min = self.color_temp_feature['value_min']
            value_max = self.color_temp_feature['value_max']

            color_object = json.loads(color)
            ct_value = value_min + int(color_object['t'] * (value_max - value_min) / self.MAX_CT_VALUE)

            return dict({
                state_value_key: self.state_feature['value_on'],
                value_key: ct_value
            }, **self.get_brightness_command(level))

        return super().generate_command(command, level, color)