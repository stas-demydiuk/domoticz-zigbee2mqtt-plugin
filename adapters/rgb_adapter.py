import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.color_light import ColorLight

class RGBAdapter(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.dimmer = ColorLight(devices, 'light', 'state_brightness_color')
        self.devices.append(self.dimmer)

    def handleCommand(self, alias, device, device_data, command, level, color):
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
            color_temp = colorObject['t']
            cwww = colorObject['cw'] + colorObject['ww']
            ttime = 1

            #only use cwww to determine mode
            if cwww == 0:
                payload = json.dumps({
                    "state": "ON",
              # Disabled the transition time for now because hue bulb/zigbee2mqtt will
              # publish (acknowledge) the new color value during the transition with
              # a value between start and end of the transition, not the actual target color
              #      "transition" : ttime,
                    "brightness": int(level * 255 / 100),
                    "color": {
                        "r": red,
                        "g": green,
                        "b": blue
                    }
                })
            else:
                payload = json.dumps({
                    "state": "ON",
               #     "transition" : ttime,
                    "color_temp": int((color_temp / 255 * 346) + 154),
                    "brightness": int(level * 255 / 100)
                })

            Domoticz.Debug('Sending to ZigBee:' + str(payload))
            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': payload
            }
