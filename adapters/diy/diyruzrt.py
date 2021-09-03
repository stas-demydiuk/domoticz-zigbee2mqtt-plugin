from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from devices.sensor.temperature import TemperatureSensor

#DIYRuZRT Sonoff ZBR3 switch + DS18b20 temperature sensor
class DIYRuZ_RT(OnOffSwitchAdapter):
    def __init__(self):
        super().__init__()
        self.devices.append(TemperatureSensor('temp', 'temperature', ' (Temperature)'))
