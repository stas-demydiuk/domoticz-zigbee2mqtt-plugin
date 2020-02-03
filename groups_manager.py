import Domoticz
import json
from zigbee_message import ZigbeeMessage
from devices.switch.on_off_switch import OnOffSwitch


class GroupsManager:
    def __init__(self):
        self.groups = {}

    def register_groups(self, domoticz_devices, groups):
        self.groups = {}

        for item in groups:
            group_id = self._get_group_address_by_name(item['friendly_name'])
            device_data = {
                'type': 'Group',
                'model': 'Group',
                'ieee_addr': group_id,
                'friendly_name': item['friendly_name']
            }

            Domoticz.Log('Group ' + item['friendly_name'] + ' (' + group_id + '_grp)')

            device = OnOffSwitch(domoticz_devices, 'grp', 'state')
            device.register(device_data)

            self.groups[group_id] = {
                'friendly_name': item['friendly_name'],
                'device': device
            }

    def _get_group_by_id(self, group_id):
        return self.groups[group_id] if group_id in self.groups else None

    def get_group_by_deviceid(self, device_id):
        return self._get_group_by_id(device_id.replace('_grp', '', 1))

    def get_group_by_name(self, friendly_name):
        return self._get_group_by_id(self._get_group_address_by_name(friendly_name))

    def handle_mqtt_message(self, group_name, message):
        group = self.get_group_by_name(group_name)

        if group == None:
            Domoticz.Debug('Group "' + group_name + '" not found')
            return None

        zigbee_message = ZigbeeMessage(message)

        device_data = {
            'ieee_addr': self._get_group_address_by_name(group_name),
            'friendly_name': group_name
        }

        group['device'].handle_message(device_data, zigbee_message)

    def handle_command(self, device, command, level, color):
        group = self.get_group_by_deviceid(device.DeviceID)

        if group == None:
            return None

        return {
            'topic': group['friendly_name'] + '/set',
            'payload': json.dumps({
                "state": command.upper()
            })
        }

    def _get_group_address_by_name(self, friendly_name):
        # Only first 14 characters of group name due to Domoticz Length limitation
        return friendly_name[0: 14]
