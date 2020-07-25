from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.motion import MotionSensor
from devices.sensor.lux import LuxSensor
from devices.sensor.temperature import TemperatureSensor


class HueMotionSensor(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(MotionSensor(devices, 'motion', 'occupancy'))
        self.devices.append(LuxSensor(devices, 'lux', 'illuminance'))
        self.devices.append(LuxSensor(devices, 'lux2', 'illuminance_lux'))
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', 'temperature'))
