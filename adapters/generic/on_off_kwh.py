from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from devices.sensor.kwh import KwhSensor


class OnOffKwhAdapter(OnOffSwitchAdapter):
    def __init__(self, devices):
        super().__init__(devices)
        values = ['power', 'energy']
        self.devices.append(KwhSensor(devices, 'kwh', values))
