from adapters.base_adapter import Adapter
from adapters.generic.mixins.cct import CCTMixin
from adapters.generic.mixins.rgb import RGBMixin
from devices.color_light import ColorLight
from devices.switch.color_temp_dimmer_switch import ColorTempDimmerSwitch

class GLC0082ID(Adapter, RGBMixin, CCTMixin):
    def __init__(self, devices):
        super().__init__(devices)

        values = ['state', 'brightness', 'color_temp']
        self.devices.append(ColorTempDimmerSwitch(devices, 'cct', values))
        self.devices.append(ColorLight(devices, 'rgb', 'state_brightness_color'))

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'color_temp' in message.raw:
            message.raw['color_temp'] = int(message.raw['color_temp'] * 255 / 500)

        return message
        
    def handleCommand(self, alias, device, device_data, command, level, color):
        if alias == 'rgb':
            topic = device_data['friendly_name'] + '/rgb/set'
            return self.set_color(topic, command, level, color)

        if alias == 'cct':
            topic = device_data['friendly_name'] + '/cct/set'
            return self.set_cct(topic, command, level, color)