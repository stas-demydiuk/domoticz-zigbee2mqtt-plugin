import domoticz
from devices.light.rgb import RGBLight

class RGBWLight(RGBLight):
    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, Type=241, Subtype=4, Switchtype=7)