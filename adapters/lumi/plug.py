import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch
from devices.voltage_sensor import VoltageSensor
from devices.kwh_sensor import KwhSensor

class Plug(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        
        self.devices.append(OnOffSwitch(devices, 'switch', 'state'))
        self.devices.append(VoltageSensor(devices, 'volt', 'voltage'))
        self.devices.append(KwhSensor(devices, 'kwh', 'power'))

    def handleCommand(self, alias, device, device_data, command, level, color):
        return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "state": command
            })
        }
                