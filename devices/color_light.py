import json
import Domoticz
from devices.device import Device

class ColorLight(Device):
    """device class for a color controllable light bulb"""

    def __init__(self, devices, alias, value_keys):
        super().__init__(devices, alias, value_keys)
        self.value_keys = value_keys.split('_') #list of capabilities as returned form MQTT, separated by '_'

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
            n_value = self.get_numeric_value(value, device)
            s_value = self.get_string_value(value, device)
        elif key == "color":
            n_value = None
            s_value = None
        
        return (s_value, n_value)

    def get_color_value(self, message):
        if 'brightness' in message.raw:
            bri=message.raw['brightness']/254
        else:
            bri=1
        colorXY = message.raw['color']
        color_values = self.get_rgb_from_xy_and_brightness(colorXY['x'],colorXY['y'],bri)
        color_value = json.dumps({
            'm': 3, #mode 3 is RGB for Domoticz
            'r': color_values[0],
            'g': color_values[1],
            'b': color_values[2]})
        return color_value
        
    def handle_message(self, device_data, message):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)
    
        Domoticz.Debug('zigbee device:' + str(device_address)+ ' sent message:' + str(message.raw))
        
        n_value = None
        s_value = None
        color_value = None

        if (device == None):
            Domoticz.Status('no device in message')
            # Due to internal domoticz bug, app crashes if we try to use device just after we create it
            # so just create and exit for now
            # device = self._create_device(device_data, message)
            return self._create_device(device_data)

        for key in self.value_keys:
            if (key not in message.raw):
                # There is no way to properly handle heartbeat messages as nValue and sValue are mandatory for device update
                Domoticz.Debug('Received heartbeat message from device "' + device.Name + '"')
                return None

            if (key != 'color'):
                value = message.raw[key]
                (s_value, n_value) = self.get_sn_values(key, value, device)
                
        signal_level = message.get_signal_level()
        battery_level = message.get_battery_level()
        
        if ("state" in message.raw and message.raw['state'].upper()=='OFF'):
            s_value = 'Off'
            n_value = 0

        if ("color" in message.raw and "color" in self.value_keys):
            color_value = self.get_color_value(message)

        #when no values in message, reuse existing values from device
        
        if (n_value == None):
            n_value = device.nValue

        if (s_value == None):
            s_value = device.sValue
            
        if (signal_level == None):
            signal_level = device.SignalLevel

        if (battery_level == None):
            battery_level = device.BatteryLevel
            
        if (color_value == None):
            color_value = device.Color
            
        Domoticz.Debug("handle_message: update device: nVal: '"+str(n_value)+"', sval: '"+s_value+"'")

        device.Update(
            nValue=n_value,
            sValue=s_value,
            SignalLevel=signal_level,
            BatteryLevel=battery_level,
            Color=color_value
        )

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