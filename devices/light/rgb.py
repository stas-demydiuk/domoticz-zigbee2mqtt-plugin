import json
import domoticz
from devices.light.ct import CTLight

class RGBLight(CTLight):
    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, Type=241, Subtype=1, Switchtype=7)

    def set_color_feature(self, feature):
        self.color_feature = feature

    def get_color_value(self, value, device):
        value_key = self.color_feature['property']
        color_mode = value['color_mode'] if 'color_mode' in value else 1

        if color_mode == 2 and self.color_temp_feature != None:
            return super().get_color_value(value, device)
        elif value_key in value: #use XY from zigbee
            brightness = self.get_brightness_value(value) or 1
            color = value[value_key]
            color_values = self.get_rgb_from_xy_and_brightness(color['x'], color['y'], brightness)

            return json.dumps({
                'm': 3, #mode 3 is RGB for Domoticz
                'r': int(color_values[0]),
                'g': int(color_values[1]),
                'b': int(color_values[2])
            })
        else:
            return device.Color

    def generate_command(self, command, level, color):
        cmd = command.upper()

        if cmd == 'SET COLOR':
            color_object = json.loads(color)

            # TODO: Consider to use 'mode' to define command type instead
            if (color_object['cw'] + color_object['ww'] == 0):
                state_value_key = self.state_feature['property']
                value_key = self.color_feature['property']

                return dict({
                    state_value_key: self.state_feature['value_on'],
                    value_key: {
                        "r": color_object['r'],
                        "g": color_object['g'],
                        "b": color_object['b']
                    }
                }, **self.get_brightness_command(level))

        return super().generate_command(command, level, color)
        
    def get_rgb_from_xy_and_brightness(self, x, y, bri=1):
        """Inverse of `get_xy_point_from_rgb`. Returns (r, g, b) for given x, y values.
        Implementation of the instructions found on the Philips Hue iOS SDK docs: http://goo.gl/kWKXKl
        """
        # Adapted from https://github.com/benknight/hue-python-rgb-converter

        # Calculate XYZ values Convert using the following formulas:
        Y = bri
        X = (Y / y) * x
        Z = (Y / y) * (1 - x - y)

        # Convert to RGB using Wide RGB D65 conversion
        r = X * 1.656492 - Y * 0.354851 - Z * 0.255038
        g = -X * 0.707196 + Y * 1.655397 + Z * 0.036152
        b = X * 0.051713 - Y * 0.121364 + Z * 1.011530

        # Apply reverse gamma correction
        r, g, b = map(
            lambda x: (12.92 * x) if (x <= 0.0031308) else ((1.0 + 0.055) * pow(x, (1.0 / 2.4)) - 0.055),
            [r, g, b]
        )

        # Bring all negative components to zero
        r, g, b = map(lambda x: max(0, x), [r, g, b])

        # If one component is greater than 1, weight components by that value.
        max_component = max(r, g, b)
        if max_component > 1:
            r, g, b = map(lambda x: x / max_component, [r, g, b])

        r, g, b = map(lambda x: int(x * 255), [r, g, b])

        # Convert the RGB values to your color object The rgb values from the above formulas are between 0.0 and 1.0.
        return (r, g, b)