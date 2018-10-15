from adapters.base_adapter import Adapter
from devices.door_contact_sensor import DoorContactSensor

class SensorMagnet(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(DoorContactSensor(devices, 'sensor', 'contact'))