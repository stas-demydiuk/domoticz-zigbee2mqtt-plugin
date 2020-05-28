from adapters.base_adapter import Adapter
from devices.sensor.voltage import VoltageSensor
from devices.sensor.percentage import PercentageSensor


class AdapterWithBattery(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(VoltageSensor(devices, 'cell', 'battery_voltage', ' (Battery Voltage)'))
        self.devices.append(PercentageSensor(devices, 'btperc', 'battery', ' (Battery)'))

    def update_battery_status(self, device_data, message):
        if 'battery_voltage' in message.raw:
            device = self.get_device_by_alias('cell')
            device.handle_message(device_data, message)

        if 'battery' in message.raw:
            device = self.get_device_by_alias('btperc')
            device.handle_message(device_data, message)

    def convert_message(self, message):
        message = super().convert_message(message)

        if 'voltage' in message.raw:
            message.raw['battery_voltage'] = message.raw['voltage'] / 1000

        return message
