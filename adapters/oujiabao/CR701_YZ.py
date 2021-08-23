from adapters.adapter_with_battery import Adapter
from devices.sensor.smoke import SmokeSensor
from devices.sensor.contact import ContactSensor


class CR701_YZ(Adapter):
    def __init__(self):
        super().__init__()
        self.devices.append(SmokeSensor('gas', 'gas'))
        self.devices.append(SmokeSensor('co', 'carbon_monoxide'))
        self.devices.append(ContactSensor('err', 'trouble'))
        self.devices.append(ContactSensor('ac', 'ac_connected'))
        self.devices.append(ContactSensor('tamper', 'tamper'))
        self.devices.append(ContactSensor('test', 'test'))

