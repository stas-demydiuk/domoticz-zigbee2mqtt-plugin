from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch
from devices.sensor.contact import ContactSensor
from devices.custom_sensor import CustomSensor
from devices.json_sensor import JSONSensor


class DJT11LM(AdapterWithBattery):
    def __init__(self):
        super().__init__()

        self.switch = SelectorSwitch('action', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Vibration', 'vibration')
        self.switch.add_level('Drop', 'drop')
        self.switch.add_level('Tilt', 'tilt')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)

        self.devices.append(self.switch)
        self.devices.append(ContactSensor('vibrtn', 'vibration', ' (Vibration)'))
        self.devices.append(CustomSensor('stgth', 'strength', ' (Strength)'))
        self.devices.append(JSONSensor('angle', 'angle_raw', ' (Angle)'))

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
