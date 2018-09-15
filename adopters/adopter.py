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

    def create_device(self, device_data):
        unit = self.get_first_available_unit()

        if (unit == None):
            Domoticz.Log('No available plugin units left to create new devices')
            return

        Domoticz.Log('Device creation has not been implemented in this adapter')

    def update_device(self, device, message):
        Domoticz.Log('Device update has not been implemented in this adapter')

    def handleMqttMessage(self, message):
        ieee_addr = message['device']['ieeeAddr']
        Domoticz.Debug('Receive message from device ' + ieee_addr)

        device = self.get_device_by_id(ieee_addr)

        if (device == None):
            Domoticz.Debug('No related device found, creating...')
            device = self.create_device(message['device'])

        if (device == None):
            Domoticz.Log('Failed to create device with ieeeAddr ' + ieee_addr)
            return

        Domoticz.Debug('Updating device "' + device.Name + '" (ID: ' + device.DeviceID + ', ieeeAddr: ' + ieee_addr + ')')
        self.update_device(device, message)

class SelectorSwitchAdopter(Adopter):
    def __init__(self, devices):
        super().__init__(devices)
        self.level_names = ['Off']

    def get_level_value(self, level_name):
        level = 0
        for item in self.level_names:
            if (level_name == item):
                return level

            level += 10

        return 0

    def create_device(self, device_data):
        unit = self.get_first_available_unit()

        if (unit == None):
            Domoticz.Log('No available plugin units left to create new devices')
            return

        ieee_addr = device_data['ieeeAddr']
        name = device_data['friendlyName']

        selector_options = {
            "LevelActions": "",
            "LevelNames": '|'.join(self.level_names),
            "LevelOffHiddden": "false",
            "SelectorStyle": "1"
        }
        
        Domoticz.Debug('Creating Aqara Cube device for ieeeAddr ' + ieee_addr)
        return Domoticz.Device(DeviceID=ieee_addr, Name=name, Unit=unit, TypeName="Selector Switch", Options=selector_options).Create()

    def update_device(self, device, message):
        signal_level = self.get_signal_level(message)
        level_name = message['action']

        device.Update(nValue=1, sValue=str(self.get_level_value(level_name)), SignalLevel=signal_level)