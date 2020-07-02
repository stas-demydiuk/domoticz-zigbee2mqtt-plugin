import Domoticz
import json

class Device():
    MAX_ALIAS_LENGTH = 6

    def __init__(self, devices, alias, value_key, device_name_suffix = ''):
        self.devices = devices
        self.alias = alias
        self.value_key = value_key
        self.device_name_suffix = device_name_suffix
        self.check_values_on_update = True

        if len(self.alias) > self.MAX_ALIAS_LENGTH:
            raise ValueError('Alias "' + self.alias + '" is too long to generate valid DeviceID')

    def get_first_available_unit(self):
        for i in range(1, 254):
            if i not in self.devices:
                return i

    def get_device(self, address, alias):
        device_id = address + '_' + alias

        for unit, device in self.devices.items():
            if device.DeviceID == device_id:
                return device

    def _create_device(self, device_data):
        device_address = device_data['ieee_addr']

        Domoticz.Debug(
            'Creating domoticz device to handle "' + self.value_key +
            '" key for device with ieeeAddr ' + device_address
        )

        device_id = device_address + '_' + self.alias
        device_name = device_data['friendly_name'] + self.device_name_suffix
        unit = self.get_first_available_unit()

        return self.create_device(unit, device_id, device_name)

    def create_device(self, unit, device_id, device_name):
        Domoticz.Error(
            'Unable to create device to handle "' + self.value_key +
            '" value for device "' + device_name + '"'
        )

    def disable_value_check_on_update(self):
        self.check_values_on_update = False

    def update_device(self, device, values):
        nValueChanged = values['nValue'] != device.nValue
        sValueChanged = values['sValue'] != device.sValue
        colorChanged = 'Color' in values and values['Color'] != device.Color

        if nValueChanged or sValueChanged or colorChanged or self.check_values_on_update == False:
            device.Update(**values)
        else:
            self.touch_device(device)

    def touch_device(self, device):
        # Touch has been added in recent Domoticz beta, so check if it exists for backward compatibility
        if hasattr(device, 'Touch') and callable(getattr(device, 'Touch')):
            device.Touch()
        else:
            Domoticz.Debug('Received heartbeat message from device "' + device.Name + '"')

    # Register device in Domoticz
    def register(self, device_data):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)

        if (device == None):
            self._create_device(device_data)

    # Removes device from Domoticz
    def remove(self, ieee_addr):
        device = self.get_device(ieee_addr, self.alias)

        if (device != None):
            device.Delete()

    def get_message_value(self, message):
        if (self.value_key in message.raw):
            return message.raw[self.value_key]
        else:
            return None

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

    def get_device_args(self, value, device, message):
        return {
            'nValue': self.get_numeric_value(value, device),
            'sValue': self.get_string_value(value, device)
        }

    def handle_message(self, device_data, message):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)
        value = self.get_message_value(message)

        if (device == None):
            # Due to internal domoticz bug, app crashes if we try to use device just after we create it
            # so just create and exit for now
            # device = self._create_device(device_data, message)
            return self._create_device(device_data)

        if (value == None):
            self.touch_device(device)
            return None

        device_values = dict({
            'BatteryLevel': message.get_battery_level() or device.BatteryLevel,
            'SignalLevel': message.get_signal_level() or device.SignalLevel,
        }, **self.get_device_args(value, device, message))
        
        self.update_device(device, device_values)

    def handle_command(self, device_data, command, level, color):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)

        Domoticz.Debug('Command "' + command + '" from device "' + device.Name + '"')
