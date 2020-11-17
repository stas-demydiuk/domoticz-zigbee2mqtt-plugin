from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from devices.sensor.current import CurrentSensor
from devices.sensor.voltage import VoltageSensor
from devices.sensor.kwh import KwhSensor


class PlugAdapter(OnOffSwitchAdapter):
    def __init__(self, devices):
        super().__init__(devices)
        
        self.devices.append(VoltageSensor(devices, 'volt', 'voltage', ' (Voltage)'))
        self.devices.append(CurrentSensor(devices, 'ampere', 'current', ' (Current)'))
        self.devices.append(KwhSensor(devices, 'power', ['power'], ' (Power)'))