import Domoticz
import json
from adapters.adapter import Adapter

class AqaraDoubleWiredSwitch(Adapter):
    def get_switch_device(self, channel, message):
        ieee_addr = message.get_device_ieee_addr()
        device_id = ieee_addr + '_' + channel

        device = self.get_device_by_id(device_id)
        
        if (device == None):
            Domoticz.Log('Creating switch ' + str(channel) + ' for device with ieeeAddr ' + ieee_addr)
            unit = self.get_first_available_unit()

            if (unit == None):
                Domoticz.Log('No available plugin units left to create new devices')
                return
            
            device_name = message.get_device_name()
            
            options = self.get_device_options(message)
            options['update_topic'] = ieee_addr + '/' + channel + '/set'

            device = Domoticz.Device(DeviceID=device_id, Name=device_name, Unit=unit, TypeName="Switch", Options=options).Create()

        return device

    def get_device(self, message):
        return {
            'left': self.get_switch_device('left', message),
            'right': self.get_switch_device('right', message)
        }

    def update_device(self, devices, message):
        signal_level = message.get_signal_level()
        battery_level = message.get_battery_level()

        for key in ['left', 'right']:
            device = devices[key] if key in devices else None
            state_key = 'state_' + key

            if device == None:
                Domoticz.Debug('Can not find device for ' + key + ' key of ' + message.get_device_name())
                continue

            Domoticz.Debug('Updating state for device ' + device.Name)

            if (state_key not in message.raw):
                n_value = device.nValue
            else:
                n_value = 1 if message.raw[state_key] == 'ON' else 0

            s_value = 'On' if n_value == 1 else 'Off'
            device.Update(nValue=n_value, sValue=s_value, SignalLevel=signal_level, BatteryLevel=battery_level)

    def handleCommand(self, device, command, level, color):
        if ('update_topic' not in device.Options):
            return

        return {
            'topic': device.Options['update_topic'],
            'payload': json.dumps({
                "state": command
            })
        }