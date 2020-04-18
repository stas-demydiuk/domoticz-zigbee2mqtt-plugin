from api.command import APICommand


class GetDevices(APICommand):
    def execute(self, params):
        self.publish_mqtt('bridge/config/devices', '')

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'devices':
            self.send_response(message['message'])