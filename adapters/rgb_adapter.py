import Domoticz
from adapters.base_adapter import Adapter
from adapters.generic.mixins.rgb import RGBMixin
from devices.color_light import ColorLight

class RGBAdapter(Adapter, RGBMixin):
    def __init__(self, devices):
        super().__init__(devices)

        self.dimmer = ColorLight(devices, 'light', 'state_brightness_color')
        self.devices.append(self.dimmer)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'color_temp' in message.raw:
            message.raw['color_temp'] = int(message.raw['color_temp'] * 255 / 500)

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        topic = device_data['friendly_name'] + '/set'
        return self.set_color(topic, command, level, color)