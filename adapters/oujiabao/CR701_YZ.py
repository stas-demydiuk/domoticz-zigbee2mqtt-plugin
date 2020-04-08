from adapters.adapter_with_battery import Adapter
from devices.sensor.smoke import SmokeSensor
from devices.sensor.contact import ContactSensor


class CR701_YZ(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(SmokeSensor(devices, 'gas', 'gas'))
        self.devices.append(SmokeSensor(devices, 'co', 'carbon_monoxide'))
        self.devices.append(ContactSensor(devices, 'err', 'trouble'))
        self.devices.append(ContactSensor(devices, 'ac', 'ac_connected'))
        self.devices.append(ContactSensor(devices, 'tamper', 'tamper'))
        self.devices.append(ContactSensor(devices, 'test', 'test'))

