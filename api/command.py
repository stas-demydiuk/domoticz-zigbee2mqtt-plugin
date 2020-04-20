import Domoticz


class APICommand():
    def __init__(self, request_id, publish_mqtt, send_response, send_update):
        self.request_id = request_id
        self.publish_mqtt = publish_mqtt
        self.execute_send_response = send_response
        self.execute_send_update = send_update

    def send_update(self, payload):
        self.execute_send_update(self.request_id, payload)

    def send_response(self, payload):
        self.execute_send_response(self.request_id, False, payload)

    def send_error(self, payload):
        self.execute_send_response(self.request_id, True, payload)

    def execute(self, params):
        Domoticz.Error('Command is not implemented')

    def handle_mqtt_message(self):
        return None
