import json
import Domoticz
from api.command import APICommand


class OtaUpdate(APICommand):
    def execute(self, params):
        Domoticz.Debug("API OTACommand for: params = '" + str(params) + "' self.request_id = '" + str(self.request_id) + "'")
        self.publish_mqtt('bridge/ota_update/update', params['state'])
        #self.send_response('ok')
        
    def handle_mqtt_message(self, topic, message):
        if topic == 'bridge/log' and message['type'] == 'ota_update':
            self.send_response(message['message'])