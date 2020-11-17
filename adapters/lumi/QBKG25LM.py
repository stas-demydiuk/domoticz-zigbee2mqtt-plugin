import Domoticz
import json
from adapters.base_adapter import Adapter
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.selector_switch import SelectorSwitch

class QBKG25LM(Adapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.endpoints = ['left', 'center', 'right']

        for button in self.endpoints:
            self.devices.append(self.create_switch(devices, button))
            self.devices.append(self.create_button(devices, button))

    def create_button(self, devices, name):
        action_prefix = name + '_'
        device = SelectorSwitch(devices, 'btn_' + name[0], 'action_' + name, ' (' + name.capitalize() + ' Button)')
        device.add_level('Off', None)
        device.add_level('Click', action_prefix + 'single')
        device.add_level('Double', action_prefix + 'double')
        device.add_level('Triple', action_prefix + 'triple')
        device.add_level('Hold', action_prefix + 'hold')
        device.add_level('Release', action_prefix + 'release')
        device.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)
        device.disable_value_check_on_update()

        return device

    def create_switch(self, devices, name):
        device = OnOffSwitch(devices, 'sw_' + name[0], 'state_' + name, ' (' + name.capitalize() + ' Switch)')
        return device

    def convert_message(self, message):
        if 'action' in message.raw:
            action = message.raw['action']

            for button in self.endpoints:
                if action.startswith(button):
                    message.raw['action_' + button] = action

        return message


    def handleCommand(self, alias, device, device_data, command, level, color):
        if alias.startswith('btn'):
            device = self.get_device_by_alias(alias)

            if device != None:
                device.handle_command(device_data, command, level, color)
        elif alias.startswith('sw'):
            device = self.get_device_by_alias(alias)

            if device != None:
                device.handle_command(device_data, command, level, color)
            else:
                Domoticz.Log('Can not find device for alias "' + alias + '"')

            endpoint = None

            for button in self.endpoints:
                if alias == 'sw_' + button[0]:
                    endpoint = button

            if endpoint != None:
                return {
                    'topic': device_data['friendly_name'] + '/' + endpoint + '/set',
                    'payload': json.dumps({
                        "state": command.upper()
                    })
                }
        else:
            return super().handleCommand(alias, device, device_data, command, level, color)