import Domoticz

class Adopter:
    def __init__(self, devices):
        self.devices = devices

    def get_device_by_id(self, id):
        for unit, device in self.devices.items():
            if device.DeviceID == id:
                return device

    def get_first_available_unit(self):
        for i in range(1, 255):
            if i not in self.devices:
                return i

    def get_signal_level(self, message):
        return int(int(message['linkquality']) * 100 / 255)

    def get_battery_level(self, message):
        power_source = message['device']['powerSource']

        if (power_source == 'Battery'):
            if ('battery' in message):
                return int(float(message['battery']))
            else:
                return None
        else:
            return 255

    def _create_device(self, device_data):
        unit = self.get_first_available_unit()

        if (unit == None):
            Domoticz.Log('No available plugin units left to create new devices')
            return

    def create_device(self, unit, device_id, device_name, device_data):
        Domoticz.Log('Device creation has not been implemented in this adapter')

    def _create_device(self, device_data):
        unit = self.get_first_available_unit()
        device_id = device_data['ieeeAddr']
        device_name = device_data['friendlyName']

        if (unit == None):
            Domoticz.Log('No available plugin units left to create new devices')
            return

        return self.create_device(unit, device_id, device_name, device_data)

    def update_device(self, device, message):
        Domoticz.Log('Device update has not been implemented in this adapter')

    def handleMqttMessage(self, message):
        ieee_addr = message['device']['ieeeAddr']
        Domoticz.Debug('Receive message from device ' + ieee_addr)

        device = self.get_device_by_id(ieee_addr)

        if (device == None):
            Domoticz.Debug('No related device found, creating...')
            device = self._create_device(message['device'])

        if (device == None):
            Domoticz.Log('Failed to create device with ieeeAddr ' + ieee_addr)
            return

        Domoticz.Debug('Updating device "' + device.Name + '" (ID: ' + device.DeviceID + ', ieeeAddr: ' + ieee_addr + ')')
        self.update_device(device, message)

class SelectorSwitchAdopter(Adopter):
    SELECTOR_TYPE_BUTTONS = 0
    SELECTOR_TYPE_MENU = 1

    def __init__(self, devices):
        super().__init__(devices)
        self.level_names = ['Off']
        self.selector_style = self.SELECTOR_TYPE_MENU

    def get_level_value(self, level_name):
        level = 0
        for item in self.level_names:
            if (level_name == item):
                return level

            level += 10

        return 0

    def get_level_name(self, message):
        Domoticz.Log('Unable to get device level name, action is not implemented in adapter')

    def create_device(self, unit, device_id, device_name, device_data):
        selector_options = {
            "LevelActions": "",
            "LevelNames": '|'.join(self.level_names),
            "LevelOffHiddden": "false",
            "SelectorStyle": "1"
        }
        
        Domoticz.Debug('Creating selector switch for device with ieeeAddr ' + device_id)
        return Domoticz.Device(DeviceID=device_id, Name=device_name, Unit=unit, TypeName="Selector Switch", Options=selector_options).Create()

    def update_device(self, device, message):
        level_value = str(self.get_level_value(self.get_level_name(message)))
        signal_level = self.get_signal_level(message)
        battery_level = self.get_battery_level(message)

        if (battery_level == None):
            battery_level = device.BatteryLevel

        device.Update(nValue=1, sValue=level_value, SignalLevel=signal_level, BatteryLevel=battery_level)