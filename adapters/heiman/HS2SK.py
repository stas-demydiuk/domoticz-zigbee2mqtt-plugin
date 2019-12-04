from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from devices.sensor.voltage import VoltageSensor
from devices.sensor.kwh import KwhSensor


class HS2SK(OnOffSwitchAdapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(VoltageSensor(devices, 'volt', 'voltage'))
        values = ['power']
        self.devices.append(KwhSensor(devices, 'kwh', values))
