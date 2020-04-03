import Domoticz
import json
import re
from zigbee_message import ZigbeeMessage
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.rgb_adapter import RGBAdapter
from adapters.rgbw_adapter import RGBWAdapter

class GroupsManager:
    def __init__(self):
        self.groups = {}

    def register_groups(self, domoticz_devices, groups):
        self.groups = {}

        for item in groups:
            group_name = item['friendly_name']
            group_id = self._get_group_address_by_name(group_name)

            device_data = {
                'type': 'Group',
                'model': 'Group',
                'ieee_addr': group_id,
                'friendly_name': group_name
            }

            Domoticz.Log('Group ' + group_name)

            adapter = self._get_adapter(domoticz_devices, group_name)
            adapter.register(device_data)

            self.groups[group_id] = {
                'friendly_name': group_name,
                'adapter': adapter
            }

    def _get_adapter(self, domoticz_devices, group_name):
        if (group_name.endswith('_dimmer')):
            adapter = DimmableBulbAdapter(domoticz_devices)
        elif (group_name.endswith('_ct')):
            adapter = DimmableCtBulbAdapter(domoticz_devices)
        elif (group_name.endswith('_rgb')):
            adapter = RGBAdapter(domoticz_devices)
        elif (group_name.endswith('_rgbw')):
            adapter = RGBWAdapter(domoticz_devices)
        else:
            adapter = OnOffSwitchAdapter(domoticz_devices)

        # Remove LinkQuality device from adapter
        adapter.devices.pop(0)
        return adapter

    def _get_group_by_id(self, group_id):
        return self.groups[group_id] if group_id in self.groups else None

    def get_group_by_deviceid(self, device_id):
        parts = device_id.split('_')
        parts.pop()
        group_id = '_'.join(parts)

        return self._get_group_by_id(group_id)

    def get_group_by_name(self, friendly_name):
        return self._get_group_by_id(self._get_group_address_by_name(friendly_name))

    def handle_mqtt_message(self, group_name, message):
        group = self.get_group_by_name(group_name)

        if group == None:
            Domoticz.Debug('Group "' + group_name + '" not found')
            return None

        adapter = group['adapter']
        zigbee_message = ZigbeeMessage(message)
        device_data = {
            'ieee_addr': self._get_group_address_by_name(group_name),
            'friendly_name': group_name
        }

        adapter.handleMqttMessage(device_data, zigbee_message)

    def handle_command(self, device, command, level, color):
        group = self.get_group_by_deviceid(device.DeviceID)

        if group == None:
            return None

        alias = device.DeviceID.split('_').pop()
        group_name = group['friendly_name']
        adapter = group['adapter']

        device_data = {
            'ieee_addr': self._get_group_address_by_name(group_name),
            'friendly_name': group['friendly_name']
        }

        return adapter.handleCommand(alias, device, device_data, command, level, color)

    def _get_group_address_by_name(self, friendly_name):
        # Only first 12 characters of group name (to match ieee address length) due to Domoticz Length limitation
        return friendly_name[0: 12]
