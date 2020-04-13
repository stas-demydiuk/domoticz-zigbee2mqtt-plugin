import json
from api.command import APICommand


class SetDeviceState(APICommand):
    def execute(self, params):
        self.publish_mqtt(params['topic'], json.dumps(params['state']))
        self.send_response('ok')