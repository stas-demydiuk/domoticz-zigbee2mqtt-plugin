from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from devices.sensor.kwh import KwhSensor


class XiaomiPlug(OnOffSwitchAdapter):
    def __init__(self, devices):
        super().__init__(devices)

        self.devices.append(KwhSensor(devices, 'kwh', ['power']))