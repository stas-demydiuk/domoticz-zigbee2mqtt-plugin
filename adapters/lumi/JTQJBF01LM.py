from adapters.adapter_with_battery import AdapterWithBattery
from devices.sensor.smoke import SmokeSensor


class JTQJBF01LM(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(SmokeSensor(devices, 'gas', 'gas'))
