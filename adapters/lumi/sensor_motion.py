import Domoticz
from adapters.adapter import Adapter

class SensorMotion(Adapter):
    def create_device(self, unit, device_id, device_name, message):
        Domoticz.Debug('Creating motion sensor for device with ieeeAddr ' + device_id)
        options = self.get_device_options(message)
        return Domoticz.Device(DeviceID=device_id, Name=device_name, Unit=unit, Type=244, Subtype=73, Switchtype=8, Options=options).Create()

    def update_device(self, device, message):
        if ('occupancy' not in message.raw):
            return

        value = message.raw['occupancy']
        signal_level = message.get_signal_level()
        battery_level = message.get_battery_level()

        if (battery_level == None):
            battery_level = device.BatteryLevel

        n_value = 1 if value else 0
        s_value = str(n_value)

        device.Update(nValue=n_value, sValue=s_value, SignalLevel=signal_level, BatteryLevel=battery_level)