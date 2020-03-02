from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class TradfriRemoteSwitchOnOff(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'click')
        self.switch.add_level('Off', 'off')
        self.switch.add_level('On', 'on')
        self.switch.add_level('Up', 'brightness_up')
        self.switch.add_level('Down', 'brightness_down')
        self.switch.add_level('Stop', 'brightness_stop')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        self.switch.disable_value_check_on_update()


        self.devices.append(self.switch)

    def handleMqttMessage(self, device_data, message):
        if 'click' not in message.raw:
            return
        converted_message = self.convert_message(message)
        click = message.raw['click']
        if click == '':
            return
        else:
            for device in self.devices:
                device.handle_message(device_data, converted_message)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
