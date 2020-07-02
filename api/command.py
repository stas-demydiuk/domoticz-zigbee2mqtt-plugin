import Domoticz


class APICommand():
    def __init__(self, request_id, on_command):
        self.request_id = request_id
        self.execute_command = on_command

    def publish_mqtt(self, topic, payload):
        self.execute_command('publish_mqtt', {
            'topic': topic,
            'payload': payload
        })

    def send_update(self, payload):
        self.execute_command('send_update', {
            'request_id': self.request_id,
            'payload': payload
        })

    def send_response(self, payload):
        self.execute_command('send_response', {
            'request_id': self.request_id,
            'payload': payload
        })

    def send_error(self, payload):
        self.execute_command('send_error', {
            'request_id': self.request_id,
            'payload': payload
        })

    def execute(self, params):
        Domoticz.Error('Command is not implemented')

    def handle_mqtt_message(self):
        return None
