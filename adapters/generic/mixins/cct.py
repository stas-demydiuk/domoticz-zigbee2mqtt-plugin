import json

class CCTMixin():
    def set_cct(self, topic, command, level, color):
        cmd = command.upper()

        if cmd == 'ON' or cmd == 'OFF':
            return {
                'topic': topic,
                'payload': json.dumps({
                    "state": command
                })
            }

        if cmd == 'SET LEVEL':
            return {
                'topic': topic,
                'payload': json.dumps({
                    "state": "ON",
                    "brightness": int(level * 255 / 100)
                })
            }

        if cmd == 'SET COLOR':
            color_object = json.loads(color)
            color_temp = color_object['t']

            return {
                'topic': topic,
                'payload': json.dumps({
                    "state": "ON",
                    "brightness": int(level * 255 / 100),
                    "color_temp": int(color_temp * 500 / 255)
                })
            }