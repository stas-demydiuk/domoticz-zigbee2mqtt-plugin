import Domoticz
from devices.device import Device


class SelectorSwitch(Device):
    SELECTOR_TYPE_BUTTONS = '0'
    SELECTOR_TYPE_MENU = '1'

    def __init__(self, devices, alias, value_key, device_name_suffix = ''):
        super().__init__(devices, alias, value_key, device_name_suffix)

        self.level_names = []
        self.level_values = []
        self.selector_style = SelectorSwitch.SELECTOR_TYPE_MENU
        self.icon = 9

    def add_level(self, name, value):
        self.level_names.append(name)
        self.level_values.append(value)

    def set_selector_style(self, selector_style):
        self.selector_style = selector_style

    def set_icon(self, icon_number):
        self.icon = icon_number

    def create_device(self, unit, device_id, device_name):
        options = {}
        options['LevelActions'] = ''
        options['LevelNames'] = '|'.join(self.level_names)
        options['LevelOffHiddden'] = 'false'
        options['SelectorStyle'] = self.selector_style

        return Domoticz.Device(Unit=unit, DeviceID=device_id, Name=device_name, TypeName="Selector Switch", Options=options, Image=self.icon).Create()

    def get_numeric_value(self, value, device):
        return 1 if self.get_string_value(value, device) != '0' else 0

    def get_string_value(self, value, device):
        try:
            index = self.level_values.index(value)
        except:
            Domoticz.Debug('Unable to find selector switch level for value "' + value + '", device: ' + device.Name)
            index = 0

        return str(index * 10)

    def handle_command(self, device_data, command, level, color):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)

        Domoticz.Debug('Command "' + command + ' (' + str(level) + ')" from device "' + device.Name + '"')

        device.Update(
            nValue=1 if level > 0 else 0,
            sValue=str(level)
        )
