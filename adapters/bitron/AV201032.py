import Domoticz
import json
from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.temperature import TemperatureSensor
from devices.switch.selector_switch import SelectorSwitch
from devices.setpoint import SetPoint


class AV201032(AdapterWithBattery):

    def __init__(self, devices):
        super().__init__(devices)

        mode_switch = SelectorSwitch(devices, 'mode', 'system_mode', ' (Mode)')
        mode_switch.add_level('Off', 'off')
        mode_switch.add_level('Auto', 'auto')
        mode_switch.add_level('Cool', 'cool')
        mode_switch.add_level('Heat', 'heat')
        mode_switch.add_level('Emergency Heating', 'emergency heating')
        mode_switch.add_level('Precooling', 'precooling')
        mode_switch.add_level('Fan only', 'fan only')
        mode_switch.add_level('Dry', 'dry')
        mode_switch.add_level('Sleep', 'sleep')
        mode_switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        mode_switch.set_icon(15)

        self.devices.append(TemperatureSensor(devices, 'temp', 'local_temperature',' (Temperature)'))
        self.devices.append(SetPoint(devices, 'sp1', 'occupied_heating_setpoint',' (Occupied Setpoint)'))
        self.devices.append(SetPoint(devices, 'sp2', 'unoccupied_heating_setpoint',' (Unoccupied Setpoint)'))
        self.devices.append(mode_switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        topic = device_data['friendly_name'] + '/set'

        if alias == 'sp1' and command == 'Set Level':
            msg = json.dumps({ 'occupied_heating_setpoint': level })

            return {
                'topic': topic,
                'payload': msg
            }

        if alias == 'sp2' and command == 'Set Level':
            msg = json.dumps({ 'unoccupied_heating_setpoint': level })

            return {
                'topic': topic,
                'payload': msg
            }

        if alias == 'mode':
            switch = self.get_device_by_alias(alias)
            level_index = int(level / 10)
            msg = json.dumps({ 'system_mode': switch.level_values[level_index] })

            return {
                'topic': topic,
                'payload': msg
            }
