from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.selector_switch import SelectorSwitch
from devices.custom_sensor import CustomSensor
from devices.json_sensor import JSONSensor
from devices.sensor.TemperatureSensor import TemperatureSensor


class DJT11LM(AdapterWithBattery):
    def __init__(self):
        super().__init__()

        selector = SelectorSwitch('action', 'action')
        selector.add_level('Off', None)
        selector.add_level('Vibration', 'vibration')
        selector.add_level('Drop', 'drop')
        selector.add_level('Tilt', 'tilt')
        selector.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)

        self.devices.append(selector)
        self.devices.append(OnOffSwitch('vibration', 'vibration', ' (Vibration)'))
        self.devices.append(CustomSensor('stgth', 'strength', ' (Strength)'))
        self.devices.append(JSONSensor('angle', 'angle_raw', ' (Angle)'))
        self.devices.append(TemperatureSensor('temp', 'device_temperature', ' (Temperature)'))

    def handle_command(self, alias, device, command, level, color):
        device_data = self._get_legacy_device_data()
        self.switch.handle_command(device_data, command, level, color)

    def convert_message(self, message):
        message = super().convert_message(message)

        message.raw['angle_raw'] = {
            'angle': message.raw['angle'],
            'angle_x': message.raw['angle_x'],
            'angle_y': message.raw['angle_y'],
            'angle_z': message.raw['angle_z'],
            'angle_x_absolute': message.raw['angle_x_absolute'],
            'angle_y_absolute': message.raw['angle_y_absolute'],
        }

        return message
