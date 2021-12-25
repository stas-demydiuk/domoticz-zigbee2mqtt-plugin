from api.command import APICommand


class NetworkMap(APICommand):
    def execute(self, params):
        self.publish_mqtt('bridge/request/networkmap', 'graphviz')

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/response/networkmap':
            if message['status'] == 'ok':
                self.send_response(message['data']['value'])
            elif message['status'] == 'error':
                self.send_error(message['error'])
            else:
                self.send_error('Unable to get zigbee network map')
