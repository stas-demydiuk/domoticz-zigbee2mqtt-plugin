from adapters.generic.temp_hum_sensor import TemperatureHumiditySensorAdapter
from devices.custom_sensor import CustomSensor

class MCLH08(TemperatureHumiditySensorAdapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(CustomSensor(devices, 'eco2', 'eco2', ' (CO2)'))
        self.devices.append(CustomSensor(devices, 'voc', 'voc', ' (Vok)'))