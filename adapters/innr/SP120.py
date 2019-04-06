from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from devices.sensor.current import CurrentSensor
from devices.sensor.voltage import VoltageSensor
from devices.custom_sensor import CustomSensor


class InnrSP120Plug(OnOffSwitchAdapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(VoltageSensor(devices, 'volt', 'voltage', ' (Voltage)'))
        self.devices.append(CurrentSensor(devices, 'ampere', 'current', ' (Current)'))
        self.devices.append(CustomSensor(devices, 'power', 'power', ' (Power)'))
