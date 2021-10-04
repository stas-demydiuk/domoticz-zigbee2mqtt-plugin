import json
import domoticz
import configuration
from adapters import adapter_by_model
from zigbee_message import ZigbeeMessage
from adapter import UniversalAdapter

class DevicesManager:
    def __init__(self):
        self.devices = {}

    def set_devices(self, zigbee_devices):
        self.devices = {}

        for item in zigbee_devices:
            device_adress = item['ieee_address']
            
            if 'type' in item and item['type'] == 'Coordinator':
                domoticz.debug('Coordinator address is ' + device_adress)
                continue

            if 'definition' not in item:
                domoticz.log(item['friendly_name'] + ': device definiton not found, skipping...')
                continue

            if item['definition'] == None:
                domoticz.log(item['friendly_name'] + ': device definiton not found, skipping...')
                continue

            if 'model' not in item['definition']:
                domoticz.log(item['friendly_name'] + ': device definiton does not contain model, skipping...')
                domoticz.debug(json.dumps(item))
                continue

            model = item['definition']['model']

            if model in adapter_by_model:
                adapter = adapter_by_model[model]()
                adapter.name = item['friendly_name']
                adapter.zigbee_device = item
                adapter.register()

                self.devices[device_adress] = adapter
            else:
                self.devices[device_adress] = UniversalAdapter(item)


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

    def handle_command(self, device_id, unit, command, level, color):
        try:
            domoticz_device = domoticz.get_device(device_id, unit)
            config = configuration.get_zigbee_feature_data(device_id, unit)
            
            alias = config['domoticz']['legacy_alias']
            device_address = config['zigbee']['address']
            adapter = self.devices[device_address]
        except:
            return

        return adapter.handle_command(alias, domoticz_device, command, level, color)


    def remove(self, friendly_name):
        adapter = self.get_device_by_name(friendly_name)

        if (adapter == None):
            return

        adapter.remove()
