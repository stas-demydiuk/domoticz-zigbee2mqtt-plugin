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
        colorXY = message.raw['color']
        color_values = self._get_RGB_from_XY(colorXY['x'],colorXY['y'],message.raw['brightness'])
        color_value = json.dumps({
            'ColorMode': 3, #mode 3: RGB
            'r': color_values[0],
            'g': color_values[1],
            'b': color_values[2]})
        return color_value
        
    def handle_message(self, device_data, message):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)
        
        n_value = None
        s_value = None
        color_value = None

        if (device == None):
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