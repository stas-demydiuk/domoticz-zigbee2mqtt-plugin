from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch
from devices.custom_sensor import CustomSensor

class SensorCube(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'cube', 'action')
        self.switch.add_level('Off', None)
        self.switch.add_level('Flip 90', 'flip90')
        self.switch.add_level('Flip 180', 'flip180')
        self.switch.add_level('Tap', 'tap')
        self.switch.add_level('Shake', 'shake')
        self.switch.add_level('Fall', 'fall')
        self.switch.add_level('Slide', 'slide')
        self.switch.add_level('Rotate Left', 'rotate_left')
        self.switch.add_level('Rotate Right', 'rotate_right')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.devices.append(self.switch)
        
        self.devices.append(CustomSensor(devices, 'angle', 'angle', ' (Rotation Angle)'))
        self.devices.append(CustomSensor(devices, 'side', 'side', ' (Side)'))
        
    def convert_message(self, message):
        message = super().convert_message(message)
	
        if 'to_side' in message.raw:
            message.raw['side'] = message.raw['to_side']

        return message


    def handle_command(self, alias, device, command, level, color):
        device_data = self._get_legacy_device_data()
        self.switch.handle_command(device_data, command, level, color)
