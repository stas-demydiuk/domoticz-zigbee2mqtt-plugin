import Domoticz
from adopters.adopter import Adopter

class Plug(Adopter):
    def get_switch_device(self, message):
        ieee_addr = message.get_device_ieee_addr()
        device_id = ieee_addr + '_0'

        device = self.get_device_by_id(device_id)
        
        if (device == None):
            Domoticz.Log('Creating switch for device with ieeeAddr ' + ieee_addr)
            unit = self.get_first_available_unit()

            if (unit == None):
                Domoticz.Log('No available plugin units left to create new devices')
                return
            
            device_name = message.get_device_name()
            device = Domoticz.Device(DeviceID=device_id, Name=device_name, Unit=unit, TypeName="Switch", Image=1).Create()

        return device

    def get_voltage_device(self, message):
        ieee_addr = message.get_device_ieee_addr()
        device_id = ieee_addr + '_1'

        device = self.get_device_by_id(device_id)
        
        if (device == None):
            Domoticz.Log('Creating voltage sensor for device with ieeeAddr ' + ieee_addr)
            unit = self.get_first_available_unit()

            if (unit == None):
                Domoticz.Log('No available plugin units left to create new devices')
                return
            
            device_name = message.get_device_name()
            device = Domoticz.Device(DeviceID=device_id, Name=device_name, Unit=unit, TypeName="Voltage").Create()

        return device

    def get_power_meter_device(self, message):
        ieee_addr = message.get_device_ieee_addr()
        device_id = ieee_addr + '_2'

        device = self.get_device_by_id(device_id)
        
        if (device == None):
            Domoticz.Log('Creating kWh sensor for device with ieeeAddr ' + ieee_addr)
            unit = self.get_first_available_unit()

            if (unit == None):
                Domoticz.Log('No available plugin units left to create new devices')
                return
            
            device_name = message.get_device_name()
            device = Domoticz.Device(DeviceID=device_id, Name=device_name, Unit=unit, TypeName="kWh").Create()

        return device

    def get_device(self, message):
        return {
            'switch': self.get_switch_device(message),
            'voltage': self.get_voltage_device(message),
            'kwh': self.get_power_meter_device(message)
        }

    def update_device(self, devices, message):
        switch_device = devices['switch']
        voltage_device = devices['voltage']
        kwh_device = devices['kwh']

        signal_level = message.get_signal_level()
        battery_level = message.get_battery_level()

        if (switch_device != None):
            if ('state' not in message.raw):
                n_value = switch_device.nValue
            else:
                n_value = 1 if message.raw['state'] == 'ON' else 0

            s_value = 'On' if n_value == 1 else 'Off'
            switch_device.Update(nValue=n_value, sValue=s_value, SignalLevel=signal_level, BatteryLevel=battery_level)

        if (voltage_device != None):
            n_value = int(message.raw['voltage']) if 'voltage' in message.raw else voltage_device.nValue
            s_value = str(n_value)

            voltage_device.Update(nValue=n_value, sValue=s_value, SignalLevel=signal_level, BatteryLevel=battery_level)

        if (kwh_device != None):
            n_value = int(message.raw['power']) if 'power' in message.raw else kwh_device.nValue
            s_value = str(n_value)

            kwh_device.Update(nValue=n_value, sValue=s_value, SignalLevel=signal_level, BatteryLevel=battery_level)
                