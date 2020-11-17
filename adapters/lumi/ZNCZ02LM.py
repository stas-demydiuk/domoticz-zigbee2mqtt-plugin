from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from devices.sensor.kwh import KwhSensor
from devices.sensor.temperature import TemperatureSensor
from devices.sensor.voltage import VoltageSensor


# Xiaomi Mi power plug
class ZNCZ02KM(OnOffSwitchAdapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.devices.append(KwhSensor(devices, 'kwh', ['power']))
        self.devices.append(VoltageSensor(devices, 'volt', 'voltage', ' (Voltage)'))
        self.devices.append(TemperatureSensor(devices, 'temp', 'temperature', ' (Temperature)'))
