import json
import Domoticz
from devices.device import Device

class BaseRGBWLight(Device):
    #Derived from dolor_light.py and color_colortemp_light.py. This class contains all common logic to control a color light. 
    #The specific device classes need to creat specific Domoticz devices and can create/override specific logics
    """base device class for a color controllable rgbw light bulb"""

    def __init__(self, devices, alias, value_keys):
        super().__init__(devices, alias, value_keys)

    def get_color_value(self, message, mode):
        if mode == 1: #mode 1 us XY from zigbee
            if 'brightness' in message.raw:
                bri=message.raw['brightness']/254
            else:
                bri=1
            colorXY = message.raw['color']
            color_values = self.get_rgb_from_xy_and_brightness(colorXY['x'],colorXY['y'],bri)
            color_value = json.dumps({
                'm': 3, #mode 3 is RGB for Domoticz
                'r': int(color_values[0]),
                'g': int(color_values[1]),
                'b': int(color_values[2])})
        elif mode == 2:
            colorTemp = int((message.raw['color_temp']-154) / 346 * 255)
            color_value = json.dumps({
                'm': 2,  # ColorModeTemp
                't': colorTemp})
        else:
            return None
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
            
        if "brightness" in message.raw:
            value=message.raw["brightness"]
            n_value = 1 if value > 0 else 0
            s_value = str(int(value * 100 / 255))
                
        signal_level = message.get_signal_level()
        
        if "state" in message.raw:
            if message.raw['state'].upper()=='OFF':
                n_value = 0
            else:
                n_value = 1

        if "color" in message.raw:
            #Colormode will be included in the message after my PR in zigbee-shepherd-converters is accepted/merged
            if "color_mode" in message.raw:
                colormode=message.raw['color_mode']
            else:
                colormode=1
            color_value = self.get_color_value(message, colormode)

        #when no values in message, reuse existing values from device
        
        payload={}
        if (n_value != None):
            payload['nValue'] = n_value

        if (s_value != None):
            payload['sValue'] = s_value
            
        if (signal_level != None):
            payload['SignalLevel'] = signal_level
            
        if (color_value != None):
            payload['Color'] = color_value
            
        Domoticz.Debug("update domticz device: '" +str(payload)+"'")

        if payload:
            if not 'nValue' in payload:
                payload['nValue'] = device.nValue
            if not 'sValue' in payload:
                payload['sValue'] = device.sValue            
            device.Update(**payload)
        else:
            Domoticz.Debug("no usable data in message... hearbeat message???")
        
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