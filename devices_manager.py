import json
import domoticz
from adapters import adapter_by_model
from zigbee_message import ZigbeeMessage
from adapter import UniversalAdapter

class DevicesManager:
    def __init__(self):
        self.devices = {}

    def set_devices(self, zigbee_devices):
        self.devices = {}

        for item in zigbee_devices:
            device_id = item['ieee_address']
            
            if 'type' in item and item['type'] == 'Coordinator':
                domoticz.debug('Coordinator address is ' + device_id)
                continue

            if 'definition' not in item:
                domoticz.error(item['friendly_name'] + ': device definiton not found')

            model = item['definition']['model']

            if model in adapter_by_model:
                adapter = adapter_by_model[model](domoticz.get_devices())
                adapter.name = item['friendly_name']
                adapter.zigbee_device = item
                adapter.register()

                self.devices[device_id] = adapter
            else:
                self.devices[device_id] = UniversalAdapter(item)


    def get_device_by_id(self, ieee_addr):
        return self.devices[ieee_addr] if ieee_addr in self.devices else None

    def get_device_by_name(self, friendly_name):
        for key, adapter in self.devices.items():
            if adapter.zigbee_device['friendly_name'] == friendly_name:
                return adapter

    def handle_mqtt_message(self, device_name, message):
        adapter = self.get_device_by_name(device_name)

        if (adapter == None):
            domoticz.debug(device_name + ': no adapter found to handle MQTT message from device')
            return

        zigbee_message = ZigbeeMessage(message)
        adapter.handle_mqtt_message(zigbee_message)

    def handle_command(self, device, command, level, color):
        device_params = device.DeviceID.split('_', 1)
        device_id = device_params[0]
        alias = device_params[1]

        adapter = self.get_device_by_id(device_id)

        if (adapter == None):
            return

        return adapter.handle_command(alias, device, command, level, color)

    def remove(self, friendly_name):
        adapter = self.get_device_by_name(friendly_name)

        if (adapter == None):
            return

        adapter.remove()
