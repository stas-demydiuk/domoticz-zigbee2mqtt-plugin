import Domoticz
from adapters import adapter_by_model
from zigbee_message import ZigbeeMessage

class DevicesManager:
    def __init__(self):
        self.devices = {}

    def _register_device(self, domoticz_devices, device_data):
        model = device_data['model']
        Domoticz.Debug('Device ' + model + ' ' + device_data['ieee_addr'] + ' (' + device_data['friendly_name'] + ')')

        self.devices[device_data['ieee_addr']] = device_data
        
        if model in adapter_by_model:
            adapter = adapter_by_model[model](domoticz_devices)
            adapter.register(device_data)

    def clear(self):
        self.devices = {}

    def update(self, domoticz_devices, zigbee_devices):
        for item in zigbee_devices:
            if 'type' in item and item['type'] == 'Coordinator':
                Domoticz.Debug('Coordinator address is ' + item['ieeeAddr'])
                continue

            friendly_name = item['friendly_name'] if 'friendly_name' in item else item['ieeeAddr']

            if 'model' in item:
                device_data = {
                    'type': item['type'],
                    'model': item['model'],
                    'ieee_addr': item['ieeeAddr'],
                    'friendly_name': friendly_name
                }

                self._register_device(domoticz_devices, device_data)
            else:
                Domoticz.Log('Device ' + item['ieeeAddr'] + ' (' + friendly_name + ') doesn\'t have "model" attribute, skipped')
                Domoticz.Log('This is not the plugin issue, this is issue with your zigbee network')
                Domoticz.Log('Try to try again later or repair the device')

    def get_device_by_id(self, ieee_addr):
        return self.devices[ieee_addr] if ieee_addr in self.devices else None

    def get_device_by_name(self, friendly_name):
        for key, device in self.devices.items():
            if (device['friendly_name'] == friendly_name):
                return device

    def handle_mqtt_message(self, domoticz_devices, device_name, message):
        device_data = self.get_device_by_name(device_name)

        if (device_data == None):
            return

        model = device_data['model']

        if (model in adapter_by_model):
            zigbee_message = ZigbeeMessage(message)
            adapter = adapter_by_model[model](domoticz_devices)
            adapter.handleMqttMessage(device_data, zigbee_message)
        else:
            Domoticz.Log('This plugin does not support zigbee device with model "' + model + '" yet')
            Domoticz.Log('If you would like plugin to support this device, please create ticket by this link: https://github.com/stas-demydiuk/domoticz-zigbee2mqtt-plugin/issues/new?labels=new+device&template=new-device-support.md')

    def handle_command(self, domoticz_devices, device, command, level, color):
        device_params = device.DeviceID.split('_')
        device_id = device_params[0]
        alias = device_params[1]

        device_data = self.get_device_by_id(device_id)

        if (device_data == None):
            return

        model = device_data['model']

        if (model in adapter_by_model):
            adapter = adapter_by_model[model](domoticz_devices)
            return adapter.handleCommand(alias, device, device_data, command, level, color)

    def remove(self, domoticz_devices, friendly_name):
        device_data = self.get_device_by_name(friendly_name)

        if (device_data == None):
            return

        model = device_data['model']

        if (model in adapter_by_model):
            adapter = adapter_by_model[model](domoticz_devices)
            adapter.remove(device_data['ieee_addr'])
