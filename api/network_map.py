from api.command import APICommand


class NetworkMap(APICommand):
    def execute(self, params):
        self.publish_mqtt('bridge/networkmap/routes', 'graphviz')

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/networkmap/graphviz':
            self.send_response(message)
