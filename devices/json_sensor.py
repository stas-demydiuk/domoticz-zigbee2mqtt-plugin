import json
from devices.text_sensor import TextSensor


class JSONSensor(TextSensor):
    def get_string_value(self, value, device):
        return json.dumps(value)
