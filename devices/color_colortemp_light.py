import json
import Domoticz
from devices.base_colortemp_light import BaseRGBWLight

class RGBWLight(BaseRGBWLight):
    """device class for a color controllable rgbw light bulb"""

    def __init__(self, devices, alias, value_keys):
        super().__init__(devices, alias, value_keys)

    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=241, Subtype=4, Switchtype=7).Create()
