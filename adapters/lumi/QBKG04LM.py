from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from devices.switch.selector_switch import SelectorSwitch


class QBKG04LM(OnOffSwitchAdapter):
    def __init__(self, devices):
        super().__init__(devices)

        selector = SelectorSwitch(devices, 'action', 'action')
        selector.add_level('Off', None)
        selector.add_level('Click', 'single')
        selector.add_level('Hold', 'hold')
        selector.add_level('Release', 'release')
        selector.disable_value_check_on_update()

        self.devices.append(selector)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'click' in message.raw and 'action' not in message.raw:
            message.raw['action'] = message.raw['click']

        return message

    def handleCommand(self, alias, device, device_data, command, level, color):
        if alias == 'switch':
            return super().handleCommand(alias, device, device_data, command, level, color)
        else:
            device = self.get_device_by_alias(alias)

            if device != None:
                device.handle_command(device_data, command, level, color)
