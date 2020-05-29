from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch
from devices.custom_sensor import CustomSensor
from devices.json_sensor import JSONSensor


class DJT11LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'action', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Vibration', 'vibration')
        self.switch.add_level('Drop', 'drop')
        self.switch.add_level('Tilt', 'tilt')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)

        self.devices.append(self.switch)
        self.devices.append(CustomSensor(devices, 'stgth', 'strength', ' (Strength)'))
        self.devices.append(JSONSensor(devices, 'angle', 'angle_raw', ' (Angle)'))

    def handleCommand(self, alias, device, device_data, command, level, color):
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
