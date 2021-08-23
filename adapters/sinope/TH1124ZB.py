import json
from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.contact import ContactSensor
from devices.sensor.temperature import TemperatureSensor
from devices.switch.selector_switch import SelectorSwitch
from devices.setpoint import SetPoint


class TH1124ZB(AdapterWithBattery):

    def __init__(self):
        super().__init__()

        self.devices.append(ContactSensor('sensor', 'contact'))
        temperature_sensor = TemperatureSensor('temp', 'local_temperature',' (Temperature)')
        self.devices.append(temperature_sensor)

        setpoint = SetPoint('sp1', 'occupied_heating_setpoint',' (Occupied Setpoint)')
        self.devices.append(setpoint)

        mode_switch = SelectorSwitch('mode', 'system_mode', ' (Mode)')
        mode_switch.add_level('Off', 'idle')
        mode_switch.add_level('Heat', 'heat')
        mode_switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        mode_switch.set_icon(15)
        self.devices.append(mode_switch)

    def handle_command(self, alias, device, command, level, color):
        topic = self.name + '/set'

        if alias == 'sp1' and command == 'Set Level':
            msg = json.dumps({ 'occupied_heating_setpoint': level })

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
