from api.command import APICommand


class GetBridgeStatus(APICommand):
    def execute(self, params):
        self.publish_mqtt('bridge/config/permit_join', '')

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/config':
            self.send_response(message)


class SetBridgePermitJoinStatus(APICommand):
    def execute(self, params):
        self.publish_mqtt('bridge/config/permit_join', params)

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/config':
            self.send_response(message)


class PairDevice(APICommand):
    def execute(self, params):
        return None

    def handle_mqtt_message(self, topic, message):
        if topic != 'bridge/log':
            return None

        if message['type'] == 'pairing' and message['message'] == 'interview_successful':
            self.send_response(message)
            return None

        if message['type'] == 'pairing' or message['type'] == 'device_connected' or message['type'] == 'device_announced':
            self.send_update(message)
