import json
import Domoticz
from devices.base_colortemp_light import BaseRGBWLight

class ColorLight(BaseRGBWLight):
    """device class for a color controllable light bulb"""

    def __init__(self, devices, alias, value_keys):
        super().__init__(devices, alias, value_keys)
        self.value_keys = value_keys.split('_') #list of capabilities as returned form MQTT, separated by '_'

    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=241, Subtype=1, Switchtype=7).Create()
