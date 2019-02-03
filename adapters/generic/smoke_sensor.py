from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.smoke import SmokeSensor


class SmokeSensorAdapter(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(SmokeSensor(devices, 'smoke', 'smoke'))
