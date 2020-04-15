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