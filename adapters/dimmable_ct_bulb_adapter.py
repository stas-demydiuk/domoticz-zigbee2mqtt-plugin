import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.switch.color_temp_dimmer_switch import ColorTempDimmerSwitch


class DimmableCtBulbAdapter(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        values = ['state', 'brightness', 'color_temp']
        self.dimmer = ColorTempDimmerSwitch(devices, 'light', values)
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
                    "brightness": int(level * 255 / 100)
                })
            }

        if cmd == 'SET COLOR':
            color_object = json.loads(color)
            color_temp = color_object['t']

            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "state": "ON",
                    "brightness": int(level * 255 / 100),
                    "color_temp": color_temp
                })
            }
