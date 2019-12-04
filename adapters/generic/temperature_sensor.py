from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.temperature import TemperatureSensor


class TemperatureSensorAdapter(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', 'temperature'))
