from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.contact import ContactSensor


class SensorArrival(AdapterWithBattery):
    def __init__(self):
        super().__init__()
        self.devices.append(ContactSensor('sensor', 'presence'))
