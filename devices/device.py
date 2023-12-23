import domoticz
import configuration
import blacklist

class Device():
    def __init__(self, alias, value_key, device_name_suffix = ''):
        self.alias = alias
        self.value_key = value_key
        self.device_name_suffix = device_name_suffix
        self.check_values_on_update = True

    def _get_feature_name(self):
        if hasattr(self, 'feature'):
            return self.feature['property']
        else:
            return self.alias

    def _get_zigbee_endpoint(self):
        try:
            return self.feature['endpoint']
        except:
            return 'n/a'

    def get_device(self, address):
        feature_name = self._get_feature_name()
        endpoint = self._get_zigbee_endpoint()
        return configuration.get_zigbee_feature_device(address, feature_name, endpoint)

    def get_legacy_device(self, address, alias):
        domoticz.debug('Trying to get legacy device ' + address + '(' + alias + ')')
        device_id = address + '_' + alias
        devices = domoticz.get_devices()

        try:
            device = list(devices[device_id].Units.values())[0]
            domoticz.debug('Success!')
            return device
        except:
            domoticz.debug('No such device found')
            return None

    def _create_device(self, device_data):
        device_address = device_data['ieee_addr']
        feature_name = self._get_feature_name()
        endpoint = self._get_zigbee_endpoint()
        alias_config = configuration.get_alias_by_zigbee(device_address, feature_name, endpoint)

        if alias_config:
            domoticz.log('Alias for handling ' + feature_name + '(endpoint: ' + str(endpoint) + ') feature of device ' + device_address + ' already exists in plugin configuration but Domoticz logical device with ID ' + alias_config['domoticz']['device_id'] + '(unit: ' + str(alias_config['domoticz']['unit']) + ') is not found. If you have removed device and want plugin to recreate it, please remove alias from configuration as well.')
            return None

        domoticz.debug(
            'Creating domoticz device to handle "' + self.value_key +
            '" key for device with ieeeAddr ' + device_address
        )

        device_id = device_address

        if self.device_name_suffix != '':
            device_name = device_data['friendly_name'] + self.device_name_suffix
        elif hasattr(self, 'feature'):
            device_name = device_data['friendly_name'] + ' (' + self.feature['property'] + ')'
        else:
            device_name = device_data['friendly_name']

        unit = configuration.get_device_available_unit(device_address)
        feature_name = self._get_feature_name()
        endpoint = self._get_zigbee_endpoint()

        if blacklist.has(device_id + '_' + feature_name):
            domoticz.debug('Device is in blacklist, skipped.')
            return None

        if unit == None:
            domoticz.error('Can not create new Domoticz device: maximum of 255 logical devices per phisical is reached.')
            return None

        device = self.create_device(unit, device_id, device_name)
        configuration.set_zigbee_feature_device(device_address, feature_name, endpoint, device_id, unit, self.alias)

        return device

    def create_device(self, unit, device_id, device_name):
        domoticz.error(
            'Unable to create device to handle "' + self.value_key +
            '" value for device "' + device_name + '"'
        )

    def disable_value_check_on_update(self):
        self.check_values_on_update = False

    def update_device(self, device, values):
        nValueChanged = 'nValue' in values and values['nValue'] != device.nValue
        sValueChanged = 'sValue' in values and values['sValue'] != device.sValue
        colorChanged = 'Color' in values and values['Color'] != device.Color

        if nValueChanged or sValueChanged or colorChanged or self.check_values_on_update == False:
            device.nValue = values['nValue']
            device.sValue = values['sValue']

            if 'LastLevel' in values:
                device.LastLevel = values['LastLevel']

            if 'SignalLevel' in values:
                device.SignalLevel = values['SignalLevel']

            if 'BatteryLevel' in values:
                device.BatteryLevel = values['BatteryLevel']

            if (colorChanged):
                device.Color = values['Color']

            device.Update(Log=True)
        else:
            self.touch_device(device)

    def touch_device(self, device):
        # Touch has been added in recent Domoticz beta, so check if it exists for backward compatibility
        if hasattr(device, 'Touch') and callable(getattr(device, 'Touch')):
            device.Touch()
        else:
            domoticz.debug('Received heartbeat message from device "' + device.Name + '"')

    # Register device in Domoticz
    def register(self, device_data):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address)

        if device != None:
            return
        
        # Try to find legacy device from plugin < 4.x version with device id "address_alias"
        device = self.get_legacy_device(device_address, self.alias)
        
        if device != None:
            feature_name = self._get_feature_name()
            device_id = device_address + '_' + self.alias
            endpoint = self._get_zigbee_endpoint()
            configuration.set_zigbee_feature_device(device_address, feature_name, endpoint, device_id, device.Unit, self.alias)
            return device
        else:
            self._create_device(device_data)

    # Removes device from Domoticz
    def remove(self, ieee_addr):
        device = self.get_device(ieee_addr)

        if (device != None):
            device.Delete()

    def get_message_value(self, message):
        if (self.value_key in message.raw):
            return message.raw[self.value_key]
        else:
            return None

    def get_numeric_value(self, value, device):
        domoticz.error(
            'Device with alias "' + self.alias + '" for key ' +
            self.value_key + ' can not calculate numeric value'
        )

    def get_string_value(self, value, device):
        domoticz.error(
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
        device = self.get_device(device_address)
        value = self.get_message_value(message)

        if (device == None):
            device = self._create_device(device_data)

        if (device == None):
            return None

        if (value == None):
            self.touch_device(device)
            return None

        try:
            device_values = dict({
                'BatteryLevel': message.get_battery_level() or device.BatteryLevel,
                'SignalLevel': message.get_signal_level() or device.SignalLevel,
            }, **self.get_device_args(value, device, message))
        except:
            domoticz.error('Can\'t calculate the value for device ' + str(device.ID) + ' from raw value "' + str(value) + '"')
            device_values = dict({})
        
        self.update_device(device, device_values)

    def handle_command(self, device_data, command, level, color):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address)

        if device != None:
            domoticz.debug('Command "' + command + '" from device "' + device.Name + '"')
