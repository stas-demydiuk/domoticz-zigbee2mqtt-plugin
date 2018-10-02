class Adapter():
    def __init__(self, devices):
        self.devices = []

    def handleMqttMessage(self, message):
        for device in self.devices:
            device.handle_message(message)