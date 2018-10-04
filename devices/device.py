import Domoticz


class Device():
    def __init__(self, devices, alias, value_key):
        self.devices = devices
        self.alias = alias
        self.value_key = value_key

    def get_first_available_unit(self):
        for i in range(1, 255):
            if i not in self.devices:
                return i

    def get_device(self, address, alias):
        for unit, device in self.devices.items():
            if (
                'address' in device.Options and
                'alias' in device.Options and
                device.Options['address'] == address and
                device.Options['alias'] == alias
            ):
                return device

    def get_device_options(self, message):
        return {
            "model": message.get_device_model(),
            "address": message.get_device_ieee_addr(),
            "alias": self.alias
        }

    def _create_device(self, message):
        Domoticz.Debug(
            'Creating domoticz device to handle ' + self.value_key +
            ' key for device with ieeeAddr ' + message.get_device_ieee_addr()
        )

        device_name = message.get_device_name()
        unit = self.get_first_available_unit()
        options = self.get_device_options(message)

        return self.create_device(unit, device_name, options, message)

    def create_device(self, unit, device_name, options, message):
        Domoticz.Error(
            'Unable to create device to handle ' + self.value_key +
            ' value for device ' + message.get_device_ieee_addr()
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

    def handle_message(self, message):
        device_address = message.get_device_ieee_addr()
        device = self.get_device(device_address, self.alias)

        if (device == None):
            # Due to internal domoticz bug, app crashes if we try to use device just after we create it
            # so just create and exit for now
            # device = self._create_device(message)
            return self._create_device(message)

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
