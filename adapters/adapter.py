import Domoticz

class Adapter:
    def __init__(self, devices):
        self.devices = devices
        self.available_units =  self._get_available_units()

    def get_device_by_id(self, id):
        for unit, device in self.devices.items():
            if device.DeviceID == id:
                return device

    def _get_available_units(self):
        available_units = []
        
        for i in range(1, 255):
            if i not in self.devices:
                available_units.append(i)

        return available_units

    def get_device_options(self, message):
        return {
            "model": message.get_device_model(),
            "address": message.get_device_ieee_addr()
        }

    def get_first_available_unit(self):
        return self.available_units.pop(0) if len(self.available_units) > 0 else None

    def create_device(self, unit, device_id, device_name, message):
        Domoticz.Log('Device creation has not been implemented in this adapter')

    def _create_device(self, message):
        unit = self.get_first_available_unit()
        device_id = message.get_device_ieee_addr()
        device_name = message.get_device_name()

        if (unit == None):
            Domoticz.Log('No available plugin units left to create new devices')
            return

        return self.create_device(unit, device_id, device_name, message)

    def get_device(self, message):
        ieee_addr = message.get_device_ieee_addr()
        device = self.get_device_by_id(ieee_addr)

        if (device == None):
            Domoticz.Debug('No related device found, creating...')
            device = self._create_device(message)

        if (device == None):
            Domoticz.Log('Failed to create device with ieeeAddr ' + ieee_addr)

        return device

    def update_device(self, device, message):
        Domoticz.Log('Device update has not been implemented in this adapter')

    def handleMqttMessage(self, message):
        ieee_addr = message.get_device_ieee_addr()
        Domoticz.Debug('Receive message from device ' + ieee_addr)

        device = self.get_device(message)
        self.update_device(device, message)

    def handleCommand(self, device, command, level, color):
        Domoticz.Log('Device update has not been implemented in this adapter')