import json
from api.command import APICommand


class GetGroups(APICommand):
    def execute(self, params):
        self.publish_mqtt('bridge/config/groups', '')

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'groups':
            self.send_response(message['message'])


class AddGroup(APICommand):
    def execute(self, params):
        self.group_name = params['friendly_name']
        self.publish_mqtt('bridge/config/add_group', json.dumps(params))

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'group_added' and message['message'] == self.group_name:
            self.send_response(message)


class RemoveGroup(APICommand):
    def execute(self, params):
        self.group_name = params
        self.publish_mqtt('bridge/config/remove_group', params)

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'group_removed' and message['message'] == self.group_name:
            self.send_response(message)


class IncludeDevice(APICommand):
    def execute(self, params):
        self.group_name = params['group']
        self.device_name = params['device']

        self.publish_mqtt('bridge/group/' + params['group'] + '/add', params['device'])

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'device_group_add' and message['message']['group'] == self.group_name:
            self.send_response(message['message'])

        if topic == 'bridge/log' and message['type'] == 'device_group_add_failed':
            self.send_response({
                'error': True,
                'message': message['message']
            })


class ExcludeDevice(APICommand):
    def execute(self, params):
        self.group_name = params['group']
        self.device_name = params['device']

        self.publish_mqtt('bridge/group/' + params['group'] + '/remove', params['device'])

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'device_group_remove' and message['message']['group'] == self.group_name:
            self.send_response(message['message'])

        if topic == 'bridge/log' and message['type'] == 'device_group_remove_failed':
            self.send_response({
                'error': True,
                'message': message['message']
            })