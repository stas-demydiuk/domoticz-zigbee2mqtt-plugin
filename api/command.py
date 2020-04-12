import Domoticz


class APICommand():
    def __init__(self, request_id, publish_mqtt, send_response):
        self.request_id = request_id
        self.publish_mqtt = publish_mqtt
        self.execute_send_response = send_response

    def send_response(self, payload):
        self.execute_send_response(self.request_id, payload)

    def execute(self, params):
        Domoticz.Error('Command is not implemented')

    def handle_mqtt_message(self):
        return None
