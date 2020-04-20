import json
from api.command import APICommand


class GetDevices(APICommand):
    def execute(self, params):
        self.publish_mqtt('bridge/config/devices', '')

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'devices':
            self.send_response(message['message'])


class GetDeviceState(APICommand):
    def execute(self, params):
        self.device = params
        self.publish_mqtt(self.device + '/get', '{"state": ""}')

    def handle_mqtt_message(self, topic, message):
        if topic == self.device:
            self.send_response(message)


class SetDeviceState(APICommand):
    def execute(self, params):
        self.publish_mqtt(params['topic'], json.dumps(params['state']))
        self.send_response('ok')


class RenameDevice(APICommand):
    def execute(self, params):
        self.publish_mqtt('bridge/config/rename', json.dumps(params))

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'device_renamed':
            self.send_response(message)


class GetDeviceOTAUpdateStatus(APICommand):
    def execute(self, params):
        self.device = params
        self.publish_mqtt('bridge/ota_update/check', self.device)

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'ota_update':
            meta = message['meta']

            if meta['device'] != self.device:
                return

            if meta['status'] == 'available':
                self.send_response(message['message'])

            if meta['status'] == 'not_available' or meta['status'] == 'check_failed' or meta['status'] == 'not_supported':
                self.send_error(message['message'])


class UpdateDeviceFirmware(APICommand):
    def execute(self, params):
        self.device = params
        self.publish_mqtt('bridge/ota_update/update', self.device)

    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'ota_update':
            meta = message['meta']

            if meta['device'] != self.device:
                return

            if meta['status'] == 'update_progress':
                # TODO: send update progress (meta['progress'] i.e. 5.13)
                self.send_update({
                    'message': message['message'],
                    'progress': meta['progress']
                })

                return

            if meta['status'] == 'update_succeeded':
                self.send_response(message['message'])