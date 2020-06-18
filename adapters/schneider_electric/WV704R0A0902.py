import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.sensor.temperature import TemperatureSensor
from devices.sensor.voltage import VoltageSensor
from devices.sensor.percentage import PercentageSensor
from devices.switch.selector_switch import SelectorSwitch
from devices.setpoint import SetPoint


class WV704R0A0902(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.devices.append(VoltageSensor(devices, 'cell', 'voltage', ' (Battery Voltage)'))
        self.devices.append(PercentageSensor(devices, 'btperc', 'battery', ' (Battery)'))
        self.devices.append(TemperatureSensor(devices, 'temp', 'local_temperature', ' (Temperature)'))
        self.devices.append(SetPoint(devices, 'spoint', 'occupied_heating_setpoint', ' (SetPoint)'))

    def handleCommand(self, alias, device, device_data, command, level, color):
        topic = device_data['friendly_name'] + '/set'

        if alias == 'spoint' and command == 'Set Level':
            msg = json.dumps({'occupied_heating_setpoint': level})

            return {
                'topic': topic,
                'payload': msg
            }
