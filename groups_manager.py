import json
import re
import domoticz
from zigbee_message import ZigbeeMessage
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.rgb_adapter import RGBAdapter
from adapters.rgbw_adapter import RGBWAdapter

class GroupsManager:
    def __init__(self):
        self.groups = {}

    def register_groups(self, groups):
        self.groups = {}

        for item in groups:
            group_name = item['friendly_name']
            group_id = self._get_group_address_by_name(group_name)

            device_data = {
                'type': 'Group',
                'definition': {
                    'model': 'Group',
                },
                'ieee_address': group_id,
                'friendly_name': group_name
            }

            domoticz.log('Group ' + group_name)

            adapter = self._get_adapter(group_name)
            adapter.name = group_name
            adapter.zigbee_device = device_data
            adapter.register()

            self.groups[group_id] = adapter

    def _get_adapter(self, group_name):
        domoticz_devices = domoticz.get_devices()

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
        if domoticz.get_plugin_config('trackLinkQuality'):
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
        adapter = self.get_group_by_name(group_name)

        if adapter == None:
            domoticz.debug('Group "' + group_name + '" not found')
            return None

        zigbee_message = ZigbeeMessage(message)
        adapter.handle_mqtt_message(zigbee_message)

    def handle_command(self, device, command, level, color):
        alias = device.DeviceID.split('_').pop()
        adapter = self.get_group_by_deviceid(device.DeviceID)

        if adapter == None:
            return None

        return adapter.handle_command(alias, device, command, level, color)

    def _get_group_address_by_name(self, friendly_name):
        # Only first 12 characters of group name (to match ieee address length) due to Domoticz Length limitation
        return friendly_name[0: 12]
