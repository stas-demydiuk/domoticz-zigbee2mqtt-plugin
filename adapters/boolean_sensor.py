import Domoticz
from adapters.adapter import Adapter

class BooleanSensor(Adapter):
    SENSOR_TYPE_CONTACT = 2
    SENSOR_TYPE_MOTION = 8
    SENSOR_TYPE_DOOR_CONTACT = 11

    def __init__(self, devices):
        super().__init__(devices)
        self.sensor_type = None
        self.senor_value_key = None

    def create_device(self, unit, device_id, device_name, message):
        if (self.sensor_type == None):
            Domoticz.Error('Sensor type is not specified in adapter')
            return

        Domoticz.Debug('Creating sensor for device with ieeeAddr ' + device_id)
        options = self.get_device_options(message)
        return Domoticz.Device(DeviceID=device_id, Name=device_name, Unit=unit, Type=244, Subtype=73, Switchtype=self.sensor_type, Options=options).Create()

    def get_device_value(self, sensor_value):
        return 1 if sensor_value else 0

    def update_device(self, device, message):
        if (self.senor_value_key == None):
            Domoticz.Error('Sensor value key is not specified in adapter')
            return

        if (self.senor_value_key in message.raw):
            sensor_value = message.raw[self.senor_value_key]
            n_value = self.get_device_value(sensor_value)
        else:
            n_value = device.nValue

        signal_level = message.get_signal_level()
        battery_level = message.get_battery_level()

        if (battery_level == None):
            battery_level = device.BatteryLevel

        s_value = str(n_value)

        device.Update(nValue=n_value, sValue=s_value, SignalLevel=signal_level, BatteryLevel=battery_level)