import json
import Domoticz
from api.command import APICommand


class OtaUpdate(APICommand):
    def execute(self, params):
        self.publish_mqtt('bridge/ota_update/update', params['state'])
        self.send_response('ok')