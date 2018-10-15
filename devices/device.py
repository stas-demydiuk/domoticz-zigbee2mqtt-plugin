import Domoticz


class Device():
    MAX_ALIAS_LENGTH = 6

    def __init__(self, devices, alias, value_key):
        self.devices = devices
        self.alias = alias
        self.value_key = value_key

        if len(self.alias) > self.MAX_ALIAS_LENGTH:
            raise ValueError('Alias "' + self.alias + '" is too long to generate valid DeviceID')

    def get_first_available_unit(self):
        for i in range(1, 255):
            if i not in self.devices:
                return i

    def get_device(self, address, alias):
        device_id = address + '_' + alias

        for unit, device in self.devices.items():
            if device.DeviceID == device_id:
                return device

    def _create_device(self, device_data, message):
        device_address = device_data['ieee_addr']

        Domoticz.Debug(
            'Creating domoticz device to handle ' + self.value_key +
            ' key for device with ieeeAddr ' + device_address
        )

        device_id = device_address + '_' + self.alias
        device_name = device_data['friendly_name']
        unit = self.get_first_available_unit()

        return self.create_device(unit, device_id, device_name, message)

    def create_device(self, unit, device_id, device_name, message):
        Domoticz.Error(
            'Unable to create device to handle ' + self.value_key +
            ' value for device "' + device_name + '"'
        )

    def get_numeric_value(self, value, device):
        Domoticz.Error(
            'Device with alias "' + self.alias + '" for key ' +
            self.value_key + ' can not calculate numeric value'
        )

    def get_string_value(self, value, device):
        Domoticz.Error(
            'Device with alias "' + self.alias + '" for key ' +
            self.value_key + ' can not calculate string value'
        )

    def handle_message(self, device_data, message):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)

        if (device == None):
            # Due to internal domoticz bug, app crashes if we try to use device just after we create it
            # so just create and exit for now
            # device = self._create_device(device_data, message)
            return self._create_device(device_data, message)

        if (self.value_key in message.raw):
            value = message.raw[self.value_key]
            n_value = self.get_numeric_value(value, device)
            s_value = self.get_string_value(value, device)
        else:
            n_value = device.nValue
            s_value = device.sValue

        signal_level = message.get_signal_level()
        battery_level = message.get_battery_level()

        if (signal_level == None):
            signal_level = device.SignalLevel

        if (battery_level == None):
            battery_level = device.BatteryLevel

        device.Update(
            nValue=n_value,
            sValue=s_value,
            SignalLevel=signal_level,
            BatteryLevel=battery_level
        )
