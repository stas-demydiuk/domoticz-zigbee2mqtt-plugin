import Domoticz
import json

class Device():
    MAX_ALIAS_LENGTH = 6

    def __init__(self, devices, alias, value_keys):
        self.devices = devices
        self.alias = alias
        self.value_keys = value_keys.split('_') #list of capabilities as returned form MQTT, separated by '_'

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

    def _create_device(self, device_data):
        device_address = device_data['ieee_addr']

        Domoticz.Debug(
            'Creating domoticz device to handle "' + "_".join(self.value_keys) +
            '" key for device with ieeeAddr ' + device_address
        )

        device_id = device_address + '_' + self.alias
        device_name = device_data['friendly_name']
        unit = self.get_first_available_unit()

        return self.create_device(unit, device_id, device_name)

    def create_device(self, unit, device_id, device_name):
        Domoticz.Error(
            'Unable to create device to handle ' + "_".join(self.value_keys) +
            ' value for device "' + device_name + '"'
        )

    # Register device in Domoticz
    def register(self, device_data):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)

        if (device == None):
            self._create_device(device_data)

    def get_numeric_value(self, value, device):
        Domoticz.Error(
            'Device with alias "' + self.alias + '" for key ' +
            "_".join(self.value_keys) + ' can not calculate numeric value'
        )

    def get_string_value(self, value, device):
        Domoticz.Error(
            'Device with alias "' + self.alias + '" for key ' +
            "_".join(self.value_keys) + ' can not calculate string value'
        )
        
    def get_color_value(self, message):
        Domoticz.Error(
            'Device with alias "' + self.alias + '" for key ' +
            "_".join(self.value_keys) + ' can not calculate color value'
        )

    def get_sn_values(self, key, value, device):
        return (self.get_string_value(value, device),self.get_numeric_value(value, device))

    def handle_message(self, device_data, message):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)
        n_value = None
        s_value = None
        color_value = None
        Domoticz.Debug("handle_message for device: '"+str(device)+"', alias: '"+self.alias+"' with # items: '"+str(len(message.raw))+"'")
        
        for item in message.raw:
            Domoticz.Debug("handle_message the message item: '"+item+"' message: '"+str(message.raw[item])+"'")

        if (device == None):
            # Due to internal domoticz bug, app crashes if we try to use device just after we create it
            # so just create and exit for now
            # device = self._create_device(device_data, message)
            return self._create_device(device_data)

        for key in self.value_keys:
            if (key not in message.raw):
                # There is no way to properly handle heartbeat messages as nValue and sValue are mandatory for device update
                Domoticz.Debug('Received heartbeat message from device "' + device.Name + '"')
                return None

            if (key != 'color'):
                value = message.raw[key]
                (s_value, n_value) = self.get_sn_values(key, value, device)
                
        signal_level = message.get_signal_level()
        battery_level = message.get_battery_level()
        
        if ("state" in message.raw and message.raw['state'].upper()=='OFF'):
            s_value = 'Off'
            n_value = 0

        if ("color" in message.raw and "color" in self.value_keys):
            color_value = self.get_color_value(message)

        #when no values in message, reuse existing values from device
        
        if (n_value == None):
            n_value = device.nValue

        if (s_value == None):
            s_value = device.sValue
            
        if (signal_level == None):
            signal_level = device.SignalLevel

        if (battery_level == None):
            battery_level = device.BatteryLevel
            
        if (color_value == None):
            color_value = device.Color
            
        Domoticz.Debug("handle_message: update device: nVal: '"+str(n_value)+"', sval: '"+s_value+"'")

        device.Update(
            nValue=n_value,
            sValue=s_value,
            SignalLevel=signal_level,
            BatteryLevel=battery_level,
            Color=color_value
        )

    def handle_command(self, device_data, command, level, color):
        device_address = device_data['ieee_addr']
        device = self.get_device(device_address, self.alias)

        Domoticz.Debug('Command "' + command + '" from device "' + device.Name + '"')
