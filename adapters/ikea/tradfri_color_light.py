import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.color_light import ColorLight

class TradfriColorLight(Adapter):
    """adapter for the IKEA Tradfri color control light"""
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(ColorLight(devices, 'dimmer', 'state_brightness_color'))
        
    def handleMqttMessage(self, device_data, message):
        for device in self.devices:
            device.handle_message(device_data, message)

    def handleCommand(self, alias, device, device_data, command, level, color):
        if command.upper() == 'ON' or command.upper() == 'OFF':
            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "state": command
                })
            }
        if command.upper() == 'SET LEVEL':
            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "state": "ON",
                    "brightness": int(level*255/100)
                })
            }
        if command.upper() == 'SET COLOR':
            Domoticz.Debug("IKEA handleCommand: build color command with: color '"+color+"'")
            brightness = level
            colorObject = json.loads(color)
            green = colorObject['g']
            red = colorObject['r']
            blue = colorObject['b']
            Domoticz.Debug("build color command with: R '"+str(red)+"', G '"+str(green)+"', B '"+str(blue)+"'")
            return {
                'topic': device_data['friendly_name'] + '/set',
                'payload': json.dumps({
                    "state": "ON",
                    "brightness": int(level*255/100),
                    "color": {
                    "r": red,
                    "g": green,
                    "b": blue}
                })
            }
