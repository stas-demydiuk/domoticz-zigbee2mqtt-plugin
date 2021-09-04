import domoticz
import json
from api.commands import commands


class API:
    def __init__(self, on_command):
        self.execute_command = on_command
        self.requests = {}

    def handle_request(self, request):
        data = json.loads(request)

        if (data['type'] == 'request'):
            request_id = data['requestId']
            domoticz.debug('[API] Request: [' + str(request_id) + '] ' + data['command'] + '(' + json.dumps(data['params']) + ')')

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
            domoticz.debug('[API] Response: [' + str(data['request_id']) + ']')
            return self._send_response(data['request_id'], False, data['payload'])
        elif command == 'send_error':
            return self._send_response(data['request_id'], True, data['payload'])
        elif command == 'send_update':
            return self._send_update(data['request_id'], data['payload'])
        else:
            return self.execute_command(command, data)

    def _get_transport_device(self):
        device = domoticz.get_device('api_transport', 255)
        
        if device == None:
            device = domoticz.create_device(
                Unit=255,
                DeviceID='api_transport',
                Name='Zigbee2MQTT API Transport',
                TypeName="Text"
            )

        return device

    def _send_data(self, data):
        transport_device = self._get_transport_device()
        transport_device.nValue = 0
        transport_device.sValue = json.dumps(data)
        transport_device.Update()        

    def _send_response(self, request_id, is_error, payload):
        if request_id in self.requests:
            del self.requests[request_id]

        self._send_data({
            'type': 'response',
            'requestId': request_id,
            'isError': is_error,
            'payload': payload
        })

    def _send_update(self, request_id, payload):
        self._send_data({
            'type': 'status',
            'requestId': request_id,
            'payload': payload
        })
