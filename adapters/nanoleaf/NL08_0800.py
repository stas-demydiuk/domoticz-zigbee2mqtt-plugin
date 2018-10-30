import json
from adapters.base_adapter import Adapter
from devices.dim_light import DimLight

class NL08_0800(Adapter):
    """adapter for the Nanoleaf Smart Ivy bulbs"""
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(DimLight(devices, 'light', 'state_brightness'))
        
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
                    "brightness": int(level*255/100)
                })
            }
