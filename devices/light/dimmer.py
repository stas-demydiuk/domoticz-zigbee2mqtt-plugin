import Domoticz
from devices.light.on_off import OnOffLight


class DimmerLight(OnOffLight):
    MAX_BRIGHTNESS = 100

    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=244, Subtype=73, Switchtype=7).Create()

    def set_brightness_feature(self, feature):
        self.brightness_feature = feature

    # Returns brigtness in 0..100 range
    def get_brightness_value(self, value):
        value_key = self.brightness_feature['property']
        value_min = self.brightness_feature['value_min']
        value_max = self.brightness_feature['value_max']
        
        if value_key in value:
            return int((value[value_key] - value_min) * self.MAX_BRIGHTNESS / (value_max - value_min))
        else:
            return None

    def get_brightness_command(self, level):
        value_key = self.brightness_feature['property']
        value_min = self.brightness_feature['value_min']
        value_max = self.brightness_feature['value_max']

        value = value_min + int(level * (value_max - value_min) / self.MAX_BRIGHTNESS)

        return {
            value_key: value
        }

    def get_numeric_value(self, value, device):
        state = self.get_state_value(value)
        brightness = self.get_brightness_value(value)

        if state != None:
            return super().get_numeric_value(self, value, device)
        elif brightness != None:
            return 1 if brightness > 0 else 0
        else:
            return device.nValue

    def get_string_value(self, value, device):
        brightness = self.get_brightness_value(value)

        if (brightness != None):
            return str(brightness)
        else:
            return device.sValue

    def generate_command(self, command, level, color):
        cmd = command.upper()

        if cmd == 'SET LEVEL':
            state_value_key = self.state_feature['property']

            return dict({
                state_value_key: self.state_feature['value_on'],
            }, **self.get_brightness_command(level))

        return super().generate_command(command, level, color)
        