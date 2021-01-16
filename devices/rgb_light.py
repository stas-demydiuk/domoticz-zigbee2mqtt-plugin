import json
import Domoticz
from devices.base_colortemp_light import BaseRGBWLight


class RGBLight(BaseRGBWLight):
    def create_device(self, unit, device_id, device_name):
        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, Type=241, Subtype=1, Switchtype=7).Create()
