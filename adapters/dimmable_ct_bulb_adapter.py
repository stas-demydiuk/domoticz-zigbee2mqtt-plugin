import Domoticz
from adapters.base_adapter import Adapter
from adapters.generic.mixins.cct import CCTMixin
from devices.switch.color_temp_dimmer_switch import ColorTempDimmerSwitch


class DimmableCtBulbAdapter(Adapter, CCTMixin):
    def __init__(self, devices):
        super().__init__(devices)

        values = ['state', 'brightness', 'color_temp']
        self.dimmer = ColorTempDimmerSwitch(devices, 'light', values)
        self.devices.append(self.dimmer)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'color_temp' in message.raw:
            message.raw['color_temp'] = int(message.raw['color_temp'] * 255 / 500)

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        topic = device_data['friendly_name'] + '/set'
        return self.set_cct(topic, command, level, color)

