from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.door_contact import DoorContactSensor
from devices.sensor.contact import ContactSensor


class SNZB04(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(DoorContactSensor(devices, 'sensor', 'contact'))
        self.devices.append(ContactSensor(devices, 'tamper', 'tamper'))
