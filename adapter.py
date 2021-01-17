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
from devices.setpoint import SetPoint
from devices.switch.dimmer_switch import DimmerSwitch
from devices.switch.level_switch import LevelSwitch
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.selector_switch import SelectorSwitch
from devices.light.on_off import OnOffLight
from devices.light.dimmer import DimmerLight
from devices.light.ct import CTLight
from devices.light.rgb import RGBLight
from devices.light.rgbw import RGBWLight
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

        self._add_features(zigbee_device['definition']['exposes'])
        self.register()

    def _add_features(self, features):
        for item in features:
            self._add_feature(item)

    def _add_feature(self, item):
        if item['type'] == 'binary':
            self.add_binary_device(item)
        elif item['type'] == 'enum':
            self._add_selector_device(item['name'][0: 5], item)
        elif item['type'] == 'numeric':
            self.add_numeric_device(item)
        elif item['type'] == 'switch':
            self._add_features(item['features'])
        elif item['type'] == 'light':
            self._add_light_feature(item)
        elif item['type'] == 'lock':
            self._add_features(item['features'])
        elif item['type'] == 'climate':
            self._add_features(item['features'])
        else:
            domoticz.error(self.name + ': can not process feature type "' + item['type'] + '"')
            domoticz.debug(json.dumps(item))

    def _add_light_feature(self, feature):
        light_features = feature['features']
        
        state = self._get_feature(light_features, 'state')
        brightness = self._get_feature(light_features, 'brightness')
        color_temp = self._get_feature(light_features, 'color_temp')
        color = self._get_feature(light_features, 'color_xy')
        
        alias = 'light'
        devices = domoticz.get_devices()

        if state and brightness and color_temp and color:
            device = RGBWLight(devices, alias)
            device.set_state_feature(state)
            device.set_brightness_feature(brightness)
            device.set_color_temp_feature(color_temp)
            device.set_color_feature(color)
        elif state and brightness and color:
            device = RGBLight(devices, alias)
            device.set_state_feature(state)
            device.set_brightness_feature(brightness)
            device.set_color_feature(color)
        elif state and brightness and color_temp:
            device = CTLight(devices, alias)
            device.set_state_feature(state)
            device.set_brightness_feature(brightness)
            device.set_color_temp_feature(color_temp)
        elif state and brightness:
            device = DimmerLight(devices, alias)
            device.set_state_feature(state)
            device.set_brightness_feature(brightness)
        elif state:
            device = OnOffLight(devices, 'switch')
            device.set_state_feature(state)
        else:
            domoticz.error(self.name + ': can not find appropriate device type to handle light feature')
            domoticz.debug(json.dumps(feature))
            
        if device:
            device.feature = feature
            self.devices.append(device)
        
        # Add rest light features
        for item in light_features:
            name = item['name']
            
            if name != 'state' and name != 'brightness' and name != 'color_temp' and name != 'color_xy':
                self._add_feature(item)

    def _add_device(self, alias, feature, device_type, device_name_suffix = ''):
        suffix = device_name_suffix if device_name_suffix != '' else (' (' + feature['name'] + ')')
        device = device_type(domoticz.get_devices(), alias, feature['property'], suffix)
        device.feature = feature

        self.devices.append(device)

    def _get_feature(self, features, feature_name):
        for item in features:
            if item['name'] == feature_name:
                return item

        return False

    def _add_selector_device(self, alias, feature, device_name_suffix = ''):
        suffix = device_name_suffix if device_name_suffix != '' else (' (' + feature['name'] + ')')
        device = SelectorSwitch(domoticz.get_devices(), alias, feature['property'], suffix)
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

        if (feature['name'] == 'battery_low' and state_access):
            self._add_device('lowbtr', feature, ContactSensor, ' (Low Battery)')
            return

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

        if (feature['name'] == 'away_mode' and state_access and write_access):
            alias = feature['endpoint'] if 'endpoint' in feature else 'away'
            self._add_device(alias, feature, OnOffSwitch)
            return

        domoticz.error(self.name + ': can not process binary item "' + feature['name'] + '"')
        domoticz.debug(json.dumps(feature))

    def add_numeric_device(self, feature):
        state_access = self._has_access(feature['access'], ACCESS_STATE)
        write_access = self._has_access(feature['access'], ACCESS_WRITE)

        if (feature['name'] == 'linkquality' and state_access):
            if domoticz.get_plugin_config('trackLinkQuality'):
                self._add_device('signal', feature, CustomSensor, ' (Link Quality)')
            return

        if (feature['name'] == 'battery' and state_access):
            if domoticz.get_plugin_config('useBatteryDevices'):
                self._add_device('btperc', feature, PercentageSensor, ' (Battery)')
            return

        if (feature['name'] == 'brightness' and state_access):
            alias = feature['endpoint'] if 'endpoint' in feature else 'light'
            self._add_device(alias, feature, DimmerSwitch)
            return

        if (feature['name'] == 'humidity' and state_access):
            self._add_device('hum', feature, HumiditySensor, ' (Humidity)')
            return

        if (feature['name'] == 'temperature' and state_access):
            self._add_device('temp', feature, TemperatureSensor, ' (Temperature)')
            return

        if (feature['name'] == 'local_temperature' and state_access):
            self._add_device('ltemp', feature, TemperatureSensor, ' (Local Temperature)')
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

        if feature['name'] == 'current_heating_setpoint' and feature['unit'] == '°C' and write_access:
            self._add_device('spoint', feature, SetPoint, ' (Setpoint)')
            return

        if (feature['name'] == 'position' and state_access):
            alias = feature['endpoint'] if 'endpoint' in feature else 'level'
            self._add_device(alias, feature, LevelSwitch)
            return

        domoticz.error(self.name + ': can not process numeric item "' + feature['name'] + '"')
        domoticz.debug(json.dumps(feature))

    def handle_command(self, alias, domoticz_device, command, level, color):
        device = self.get_device_by_alias(alias)

        if (device == None) :
            return

        feature = device.feature
        write_access = self._has_access(feature['access'], ACCESS_WRITE) if 'access' in feature else False

        # Optimistic update
        device_data = self._get_legacy_device_data()
        device.handle_command(device_data, command, level, color)

        if (feature['type'] == 'binary' and write_access):
            topic = self.name + '/' + ((feature['endpoint'] + '/set') if 'endpoint' in feature else 'set')
            key = feature['property']
            value = feature['value_on'] if command.upper() == 'ON' else feature['value_off']
                
            return {
                'topic': topic,
                'payload': json.dumps({
                    key: value
                })
            }

        if feature['type'] == 'numeric' and feature['name'] == 'current_heating_setpoint' and feature['unit'] == '°C' and write_access and command == 'Set Level':
            topic = self.name + '/' + ((feature['endpoint'] + '/set') if 'endpoint' in feature else 'set')
            msg = json.dumps({ feature['property']: level })

            return {
                'topic': topic,
                'payload': msg
            }

        if feature['type'] == 'numeric' and feature['name'] == 'brightness' and write_access:
            cmd = command.upper()
            topic = self.name + '/' + ((feature['endpoint'] + '/set') if 'endpoint' in feature else 'set')

            if (cmd == 'SET LEVEL'):
                value_max = feature['value_max'] if 'value_max' in feature else 255
                msg = { feature['property']: int(level * value_max / 100) }
            elif (cmd == 'ON' or cmd == 'OFF'):
                msg = { 'state': cmd }

            return {
                'topic': topic,
                'payload': json.dumps(msg)
            }

        if feature['type'] == 'enum' and write_access:
            topic = self.name + '/' + ((feature['endpoint'] + '/set') if 'endpoint' in feature else 'set')
            level_index = int(level / 10)
            msg = json.dumps({ feature['property']: device.level_values[level_index] })

            return {
                'topic': topic,
                'payload': msg
            }

        if feature['type'] == 'light':
            state_feature = device.state_feature
            topic = self.name + '/' + ((state_feature['endpoint'] + '/set') if 'endpoint' in state_feature else 'set')

            return {
                'topic': topic,
                'payload': json.dumps(device.generate_command(command, level, color))
            }

        return None
