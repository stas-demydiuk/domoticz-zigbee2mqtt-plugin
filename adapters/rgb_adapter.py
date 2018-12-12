import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.color_light import ColorLight


class RGBAdapter(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.dimmer = ColorLight(devices, 'light', 'state_brightness_color')
        self.devices.append(self.dimmer)

    def handleCommand(self, alias, device, device_data, command, level, color, config):
        cmd = command.upper()

        if cmd == 'ON' or cmd == 'OFF':
            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "state": command
                })
            }

        if cmd == 'SET LEVEL':
            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "state": "ON",
                    "brightness": int(level*255/100)
                })
            }

        if cmd == 'SET COLOR':
            colorObject = json.loads(color)
            green = colorObject['g']
            red = colorObject['r']
            blue = colorObject['b']

            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "state": "ON",
                    "brightness": int(level * 255 / 100),
                    "color": {
                        "r": red,
                        "g": green,
                        "b": blue
                    }
                })
            }
