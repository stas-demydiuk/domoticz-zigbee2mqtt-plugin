import json
import bridge
from api.command import APICommand


class GetBridgeStatus(APICommand):
    def execute(self, params):
        self.send_response(bridge.bridge_info)
        
class SetBridgePermitJoinStatus(APICommand):
    def execute(self, params):
        self.publish_mqtt('bridge/request/permit_join', json.dumps({
            'value': params
        }))

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/response/permit_join':
            self.send_response(message['data']['value'])


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
