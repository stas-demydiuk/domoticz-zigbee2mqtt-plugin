import Domoticz
import json
from api.commands import commands


class API:
    def __init__(self, devices, publish_mqtt):
        self.unit = 255
        self.devices = devices
        self._publish_mqtt = publish_mqtt
        self._create_transport()
        self.requests = {}

    def handle_request(self, request):
        data = json.loads(request)

        if (data['type'] == 'request'):
            request_id = data['requestId']
            Domoticz.Debug('New request: [' + str(request_id) + '] ' + data['command'] + '(' + json.dumps(data['params']) + ')')

            if data['command'] in commands:
                command = commands[data['command']](
                    request_id,
                    self._publish_mqtt,
                    self._send_response
                )

                command.execute(data['params'])
                self.requests.update({request_id: command})
            else:
                self._send_response(data['requestId'], 'unknown command')

    def handle_mqtt_message(self, topic, message):
        commands = list(self.requests.values())

        for command in commands:
            command.handle_mqtt_message(topic, message)

    def _create_transport(self):
        if self.unit in self.devices:
            return

        Domoticz.Device(
            Unit=self.unit,
            DeviceID='api_transport',
            Name='Zigbee2MQTT API Transport',
            TypeName="Text"
        ).Create()

    def _send_response(self, request_id, payload):
        del self.requests[request_id]

        response = json.dumps({
            'type': 'response',
            'requestId': request_id,
            'payload': payload
        })

        self.devices[self.unit].Update(
            nValue=0,
            sValue=response
        )
