from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from devices.sensor.current import CurrentSensor
from devices.sensor.voltage import VoltageSensor
from devices.sensor.kwh import KwhSensor


class InnrSP120Plug(OnOffSwitchAdapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(VoltageSensor(devices, 'volt', 'voltage', ' (Line Voltage)'))
        self.devices.append(CurrentSensor(devices, 'amper', 'current', ' (Line Current)'))
        self.devices.append(KwhSensor(devices, 'power', 'power', ' (Power)'))
