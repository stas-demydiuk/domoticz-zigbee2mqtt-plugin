import json
import domoticz
from adapters.base_adapter import Adapter
from devices.sensor.contact import ContactSensor
from devices.sensor.current import CurrentSensor
from devices.sensor.humidity import HumiditySensor
from devices.sensor.motion import MotionSensor
from devices.sensor.percentage import PercentageSensor
from devices.sensor.pressure import PressureSensor
from devices.sensor.temperature import TemperatureSensor
from devices.sensor.voltage import VoltageSensor
from devices.sensor.water_leak import WaterLeakSensor
from devices.sensor.kwh import KwhSensor
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.selector_switch import SelectorSwitch
from devices.custom_sensor import CustomSensor

ACCESS_STATE = 0
ACCESS_WRITE = 1
ACCESS_READ = 2

class UniversalAdapter(Adapter):
    def __init__(self, zigbee_device):
        self.devices = []
        self.zigbee_device = zigbee_device
        self.name = zigbee_device['friendly_name']

        if 'exposes' not in zigbee_device['definition']:
            domoticz.error(self.name + ': device exposes not found')
            return

        self._add_devices(zigbee_device['definition']['exposes'])
        self.register()

    def _add_devices(self, items):
        for item in items:
            if item['type'] == 'binary':
                self.add_binary_device(item)
                continue

            if item['type'] == 'enum':
                self._add_selector_device(item['name'], item)
                continue

            if item['type'] == 'numeric':
                self.add_numeric_device(item)
                continue

            if item['type'] == 'switch':
                self._add_devices(item['features'])
                continue

            domoticz.error(self.name + ': can not process feature type "' + item['type'] + '"')
            domoticz.debug(json.dumps(item))

    def _add_device(self, alias, feature, device_type, device_name_suffix = ''):
        device = device_type(domoticz.get_devices(), alias, feature['property'], device_name_suffix)
        device.feature = feature

        self.devices.append(device)

    def _add_selector_device(self, alias, feature, device_name_suffix = ''):
        device = SelectorSwitch(domoticz.get_devices(), alias, feature['property'], device_name_suffix)
        device.disable_value_check_on_update()
        device.add_level('Off', None)
        for value in feature['values']:
            device.add_level(value, value)

        if (len(feature['values']) >= 5):
            device.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)

        device.feature = feature

        self.devices.append(device)

    def _has_access(self, access, access_type):
        mask = 1 << access_type
        return bool(access & mask)

    def add_binary_device(self, feature):
        state_access = self._has_access(feature['access'], ACCESS_STATE)
        write_access = self._has_access(feature['access'], ACCESS_WRITE)

        if (feature['name'] == 'contact' and state_access):
            self._add_device('sensor', feature, ContactSensor)
            return

        if (feature['name'] == 'occupancy' and state_access):
            self._add_device('motion', feature, MotionSensor)
            return

        if (feature['name'] == 'water_leak' and state_access):
            self._add_device('wleak', feature, WaterLeakSensor)
            return

        if (feature['name'] == 'tamper' and state_access):
            self._add_device('tamper', feature, ContactSensor)
            return

        if (feature['name'] == 'state' and state_access and write_access):
            alias = feature['endpoint'] if 'endpoint' in feature else 'state'
            self._add_device(alias, feature, OnOffSwitch)
            return

        domoticz.error(self.name + ': can not process binary item "' + feature['name'] + '"')
        domoticz.debug(json.dumps(feature))

    def add_numeric_device(self, feature):
        state_access = self._has_access(feature['access'], ACCESS_STATE)

        if (feature['name'] == 'linkquality' and state_access):
            # self._add_device('signal', feature, CustomSensor, ' (Link Quality)')
            return

        if (feature['name'] == 'battery' and state_access):
            if domoticz.get_plugin_config('useBatteryDevices'):
                self._add_device('btperc', feature, PercentageSensor, ' (Battery)')
            return

        if (feature['name'] == 'humidity' and state_access):
            self._add_device('hum', feature, HumiditySensor, ' (Humidity)')
            return

        if (feature['name'] == 'temperature' and state_access):
            self._add_device('temp', feature, TemperatureSensor, ' (Temperature)')
            return

        if (feature['name'] == 'pressure' and state_access):
            self._add_device('pres', feature, PressureSensor, ' (Pressure)')
            return

        if (feature['name'] == 'voltage' and state_access):
            self._add_device('volt', feature, VoltageSensor, ' (Voltage)')
            return

        if (feature['name'] == 'current' and state_access):
            self._add_device('ampere', feature, CurrentSensor, ' (Current)')
            return

        if (feature['name'] == 'power' and state_access and feature['unit'] == 'W'):
            device = KwhSensor(domoticz.get_devices(), 'power', [feature['property']], ' (Power)')
            device.feature = feature
            self.devices.append(device)
            return

        domoticz.error(self.name + ': can not process numeric item "' + feature['name'] + '"')
        domoticz.debug(json.dumps(feature))

    def handle_command(self, alias, domoticz_device, command, level, color):
        device = self.get_device_by_alias(alias)

        if (device == None) :
            return

        feature = device.feature
        write_access = self._has_access(feature['access'], ACCESS_WRITE)

        if (feature['type'] == 'binary' and write_access):
            topic = self.name + '/' + ((feature['endpoint'] + '/set') if 'endpoint' in feature else 'set')
            value = feature['value_on'] if command.upper() == 'ON' else feature['value_off']
                
            return {
                'topic': topic,
                'payload': json.dumps({
                    "state": value
                })
            }


        return None