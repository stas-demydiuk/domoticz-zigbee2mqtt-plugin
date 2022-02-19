import json
import domoticz
from devices.device import Device


class ColorTempDimmerSwitch(Device):
    def __init__(self, alias, value_key, device_name_suffix=''):
        super().__init__(alias, ';'.join(value_key), device_name_suffix)
        self.value_keys = value_key

    def create_device(self, unit, device_id, device_name):
        return domoticz.create_device(Unit=unit, DeviceID=device_id, Name=device_name, Type=241, Subtype=8, Switchtype=7)

    def get_message_value(self, message):
        value = {}

        for item in self.value_keys:
            if item in message.raw:
                value[item] = message.raw[item]

        return value if len(value) > 0 else None

    def get_numeric_value(self, value, device):
        if 'state' in value:
            return 1 if value['state'].upper() == 'ON' else 0
        else:
            return device.nValue

    def get_string_value(self, value, device):
        if 'brightness' in value:
            return str(int(value['brightness'] * 100 / 255))
        else:
            return device.sValue

    def get_color_value(self, value, device):
        if 'color_temp' in value:
            return json.dumps({
                'm': 2,  # ColorModeTemp
                't': value['color_temp']
            })
        else:
            return device.Color

    def get_device_args(self, value, device, message):
        args = super().get_device_args(value, device, message)

        return dict(args, Color=self.get_color_value(value, device))
