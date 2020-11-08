import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch
from devices.sensor.kwh import KwhSensor
from devices.sensor.temperature import TemperatureSensor

class LLKZMK11LM(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.devices.append(OnOffSwitch(devices, 'l1', 'state_l1'))
        self.devices.append(OnOffSwitch(devices, 'l2', 'state_l2'))
        values = ['power', 'consumption']
        self.devices.append(KwhSensor(devices, 'kwh', values))
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature'))

    def handle_command(self, alias, device, command, level, color):
        return {
            'topic': '/'.join([self.name, alias, 'set']),
            'payload': json.dumps({
                "state": command.upper()
            })
        }