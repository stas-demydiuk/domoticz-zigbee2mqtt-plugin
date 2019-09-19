import Domoticz
import json
from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.temperature import TemperatureSensor
from devices.setpoint import SetPoint


class ThermostatAdapter(AdapterWithBattery):

    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temp', 'local_temperature',' (Temperature)'))
        self.devices.append(SetPoint(devices, 'spoint', 'current_heating_setpoint',' (Setpoint)'))

    def handleCommand(self, alias, device, device_data, command, level, color):
        if command == 'Set Level':
            _topic = device_data['friendly_name'] + '/set'
            _msg = json.dumps({ 'current_heating_setpoint': level })
            return {
                'topic': _topic,
                'payload': _msg
            }
