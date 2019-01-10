from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.motion import MotionSensor
from devices.sensor.temperature import TemperatureSensor


class SensorMotionOsram(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(MotionSensor(devices, 'motion', 'occupancy'))
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', 'temperature'))
