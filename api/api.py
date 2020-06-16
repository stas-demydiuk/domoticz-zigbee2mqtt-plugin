import Domoticz
import json
from api.commands import commands


class API:
    def __init__(self, devices, on_command):
        self.unit = 255
        self.devices = devices
        self.execute_command = on_command

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
                    self._handle_api_command,
                )

                self.requests.update({request_id: command})
                command.execute(data['params'])
            else:
                self._send_response(data['requestId'], True, 'unknown command')
    
    def handle_mqtt_message(self, topic, message):
        commands = list(self.requests.values())

        for command in commands:
            command.handle_mqtt_message(topic, message)

    def _handle_api_command(self, command, data):
        if command == 'send_response':
            return self._send_response(data['request_id'], False, data['payload'])
        elif command == 'send_error':
            return self._send_response(data['request_id'], True, data['payload'])
        elif command == 'send_update':
            return self._send_update(data['request_id'], data['payload'])
        else:
            return self.execute_command(command, data)

    def _create_transport(self):
        if self.unit in self.devices:
            return

        Domoticz.Device(
            Unit=self.unit,
            DeviceID='api_transport',
            Name='Zigbee2MQTT API Transport',
            TypeName="Text"
        ).Create()

    def _send_response(self, request_id, is_error, payload):
        if request_id in self.requests:
            del self.requests[request_id]

        response = json.dumps({
            'type': 'response',
            'requestId': request_id,
            'isError': is_error,
            'payload': payload
        })

        self.devices[self.unit].Update(
            nValue=0,
            sValue=response
        )

    def _send_update(self, request_id, payload):
        response = json.dumps({
            'type': 'status',
            'requestId': request_id,
            'payload': payload
        })

        self.devices[self.unit].Update(
            nValue=0,
            sValue=response
        )
