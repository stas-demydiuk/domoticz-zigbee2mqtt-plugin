from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from devices.sensor.kwh import KwhSensor
from devices.sensor.current import CurrentSensor
from devices.sensor.voltage import VoltageSensor
from devices.sensor.temperature import TemperatureSensor


class DinrailAdapter(OnOffSwitchAdapter):
    def __init__(self):
        super().__init__()

        kwh_consumed = KwhSensor('cons', ['power', 'energyconsumed'], ' (Consumed)')
        kwh_consumed.energy_multiplier = 1

        kwh_produced = KwhSensor('prod', ['power', 'energyproduced'], ' (Produced)')
        kwh_produced.energy_multiplier = 1

        self.devices.append(TemperatureSensor('temp', 'temperature', ' (Temperature)'))
        self.devices.append(VoltageSensor('volt', 'voltage', ' (Voltage)'))
        self.devices.append(CurrentSensor('ampere', 'current', ' (Current)'))
        self.devices.append(kwh_consumed)
        self.devices.append(kwh_produced)
