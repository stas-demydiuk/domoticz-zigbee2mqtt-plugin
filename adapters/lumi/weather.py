import Domoticz
import json
from adapters.adapter import Adapter

class Weather(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.sensors = ['temperature', 'humidity', 'pressure']

    def create_device(self, device_id, message, type_name):
        unit = self.get_first_available_unit()

        if (unit == None):
            Domoticz.Error('No available plugin units left to create new devices')
            return
        
        device_name = message.get_device_name()
        options = self.get_device_options(message)
        return Domoticz.Device(DeviceID=device_id, Name=device_name, Unit=unit, TypeName=type_name, Options=options).Create()

    def get_device_by_type(self, message, sensor_type):
        ieee_addr = message.get_device_ieee_addr()
        index = self.sensors.index(sensor_type)
        device_id = ieee_addr + '_' + str(index)

        device = self.get_device_by_id(device_id)

        if (device == None):
            Domoticz.Log('Creating ' + sensor_type + ' sensor for device with ieeeAddr ' + ieee_addr)
            device = self.create_device(device_id, message, sensor_type.capitalize())
           
        return device

    def get_device(self, message):
        devices = {}
        
        for sensor_type in self.sensors:
            devices[sensor_type] = self.get_device_by_type(message, sensor_type)

        return devices

    def update_device(self, devices, message):
        signal_level = message.get_signal_level()
        battery_level = message.get_battery_level()

        for sensor_type in self.sensors:
            device = devices[sensor_type]

            if device == None:
                Domoticz.Debug('Can not find device for ' + sensor_type + ' sensor of ' + message.get_device_name())
                continue

            if (battery_level == None):
                battery_level = device.BatteryLevel

            if (sensor_type in message.raw):
                if (sensor_type == 'humidity'):
                    n_value = int(message.raw[sensor_type])
                    s_value = '0'
                else:
                    n_value = 0
                    s_value = str(message.raw[sensor_type])
            else:
                n_value = device.nValue
                s_value = device.sValue

            device.Update(nValue=n_value, sValue=s_value, SignalLevel=signal_level, BatteryLevel=battery_level)
                