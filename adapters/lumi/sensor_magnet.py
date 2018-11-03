from adapters.adapter_with_battery import AdapterWithBattery
from devices.door_contact_sensor import DoorContactSensor


class SensorMagnet(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(DoorContactSensor(devices, 'sensor', 'contact'))
