import json
from api.command import APICommand


class RenameDevice(APICommand):
    def execute(self, params):
        self.publish_mqtt('bridge/config/rename', json.dumps(params))

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'device_renamed':
            self.send_response(message)