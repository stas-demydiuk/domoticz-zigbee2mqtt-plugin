import json
import Domoticz
from devices.device import Device

class ColorLight(Device):
    """device class for a color controllable light bulb"""
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=241, Subtype=1, Switchtype=7).Create()

    def get_numeric_value(self, value, device):
        return 1 if value > 0 else 0

    def get_string_value(self, value, device):
        return str(int(value * 100 / 255))
        
    def get_sn_values(self, key, value, device):
        s_value = None
        n_value = None
        if key == "state" and value.upper() == 'OFF':
            n_value = 0
            s_value = value
        elif key == "brightness":
            n_value = 1 if value > 0 else 0
            s_value = str(int(value * 100 / 255))
        elif key == "color":
            n_value = None
            s_value = None
        
        return (s_value,n_value)

    def get_color_value(self, message):
        colorXY = message.raw['color']
        color_values = self._get_RGB_from_XY(colorXY['x'],colorXY['y'],message.raw['brightness'])
        color_value = json.dumps({
            'ColorMode': 3, #mode 3: RGB
            'r': color_values[0],
            'g': color_values[1],
            'b': color_values[2]})
        return color_value
        
    def _get_RGB_from_XY(self, x, y, brightness):
        """calculate RGB valus from the XY as reported by the bridge"""
        #Calculate XYZ values Convert using the following formulas
        z = 1.0 - x - y
        Y = brightness
        X = (Y/y) * x
        Z = (Y/y) * z
        #Convert to RGB using Wide RGB D65 conversion (THIS IS A D50 conversion currently)
        r = X * 1.4628067 - Y * 0.1840623 - Z * 0.2743606
        g = -X * 0.5217933 + Y * 1.4472381 + Z * 0.0677227
        b = X * 0.0349342 - Y * 0.0968930 + Z * 1.2884099
        #Apply reverse gamma correction
        
        R = 12.92 * r if r <= 0.0031308 else (1.0 + 0.055) * pow(r, (1.0 / 2.4)) - 0.055
        G = 12.92 * g if g <= 0.0031308 else (1.0 + 0.055) * pow(g, (1.0 / 2.4)) - 0.055
        B = 12.92 * b if b <= 0.0031308 else (1.0 + 0.055) * pow(b, (1.0 / 2.4)) - 0.055
        return (R,G,B)