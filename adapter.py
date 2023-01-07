import json
import domoticz
from adapters.base_adapter import Adapter
from devices.sensor.contact import ContactSensor
from devices.sensor.co2 import CO2Sensor
from devices.sensor.current import CurrentSensor
from devices.sensor.lux import LuxSensor
from devices.sensor.motion import MotionSensor
from devices.sensor.percentage import PercentageSensor
from devices.sensor.smoke import SmokeSensor
from devices.sensor.temperature import TemperatureSensor
from devices.sensor.voltage import VoltageSensor
from devices.sensor.water_leak import WaterLeakSensor
from devices.setpoint import SetPoint
from devices.switch.dimmer_switch import DimmerSwitch
from devices.switch.level_switch import LevelSwitch
from devices.switch.on_off_switch import OnOffSwitch
from devices.switch.selector_switch import SelectorSwitch
from devices.switch.siren_switch import SirenSwitch
from devices.custom_sensor import CustomSensor
from features.cover import CoverFeatureProcessor
from features.energy import EnergyFeatureProcessor
from features.light import LightFeatureProcesor
from features.temp_hum_pressure import TempHumPressureFeatureProcessor

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

        self.feature_processors = [
            CoverFeatureProcessor(self),
            EnergyFeatureProcessor(),
            LightFeatureProcesor(self),
            TempHumPressureFeatureProcessor(),
        ]

        self._add_features(zigbee_device['definition']['exposes'])
        self.register()

    def _add_features(self, features):
        for processor in self.feature_processors:
            devices = processor.register(features)
            self.devices.extend(devices)

        for item in features:
            if 'name' in item and item['name'] in ['energy', 'power', 'temperature', 'humidity', 'pressure']:
                continue
            else:
                self._add_feature(item)

    def _add_feature(self, item):
        # Avoid creating devices for settings as it is ususally one-time op
        if 'name' in item and item['name'] in ['temperature_offset', 'humidity_offset', 'pressure_offset', 'local_temperature_calibration', 'temperature_setpoint_hold_duration']:
            return

        if item['type'] == 'binary':
            self.add_binary_device(item)
        elif item['type'] == 'enum':
            self._add_selector_device(item['name'][0: 5], item)
        elif item['type'] == 'numeric':
            self.add_numeric_device(item)
        elif item['type'] == 'switch':
            self._add_features(item['features'])
        elif item['type'] == 'light':
            return None
        elif item['type'] == 'lock':
            self._add_features(item['features'])
        elif item['type'] == 'climate':
            self._add_features(item['features'])
        elif item['type'] == 'cover':
            return None
        else:
            domoticz.debug(self.name + ': can not process feature type "' + item['type'] + '"')
            domoticz.debug(json.dumps(item))

    def _add_device(self, alias, feature, device_type, device_name_suffix = ''):
        suffix = device_name_suffix if device_name_suffix != '' else (' (' + feature['name'] + ')')
        device = device_type(alias, feature['property'], suffix)
        device.feature = feature

        self.devices.append(device)
        return device

    def _get_feature(self, features, feature_name):
        for item in features:
            if 'name' in item and item['name'] == feature_name:
                return item

        return False

    def _add_selector_device(self, alias, feature, device_name_suffix = ''):
        suffix = device_name_suffix if device_name_suffix != '' else (' (' + feature['name'] + ')')
        device = SelectorSwitch(alias, feature['property'], suffix)
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

    def _generate_alias(self, feature, default_value):
        if 'endpoint' in feature:
            return feature['endpoint']
        else:
            return default_value

    def add_binary_device(self, feature):
        state_access = self._has_access(feature['access'], ACCESS_STATE)
        write_access = self._has_access(feature['access'], ACCESS_WRITE)

        if (feature['name'] == 'alarm' and state_access and write_access):
            alias = self._generate_alias(feature, 'alarm')
            self._add_device(alias, feature, SirenSwitch)
            return

        if (feature['name'] == 'battery_low' and state_access):
            alias = self._generate_alias(feature, 'lowbtr')
            self._add_device(alias, feature, ContactSensor, ' (Low Battery)')
            return

        if (feature['name'] == 'contact' and state_access):
            alias = self._generate_alias(feature, 'sensor')
            self._add_device(alias, feature, ContactSensor)
            return

        if (feature['name'] == 'charging_status' and state_access):
            alias = self._generate_alias(feature, 'chrgst')
            self._add_device(alias, feature, ContactSensor, ' (Charging Status)')
            return

        if (feature['name'] == 'gas' and state_access):
            alias = self._generate_alias(feature, 'gas')
            self._add_device(alias, feature, SmokeSensor, ' (Gas sensor)')
            return

        if (feature['name'] == 'occupancy' and state_access):
            alias = self._generate_alias(feature, 'motion')
            self._add_device(alias, feature, MotionSensor)
            return

        if (feature['name'] == 'presence' and state_access):
            alias = self._generate_alias(feature, 'motion')
            self._add_device(alias, feature, MotionSensor)
            return

        if (feature['name'] == 'smoke' and state_access):
            alias = self._generate_alias(feature, 'smoke')
            self._add_device(alias, feature, SmokeSensor, ' (Smoke sensor)')
            return

        if (feature['name'] == 'water_leak' and state_access):
            alias = self._generate_alias(feature, 'wleak')
            self._add_device(alias, feature, WaterLeakSensor)
            return

        if (feature['name'] == 'window' and state_access):
            alias = self._generate_alias(feature, 'window')
            self._add_device(alias, feature, ContactSensor, ' (Window Closed Status)')
            return

        if (feature['name'] == 'heating' and state_access):
            alias = self._generate_alias(feature, 'heating')
            device = self._add_device(alias, feature, ContactSensor, ' (Heating)')
            device.set_icon(15)
            return

        if (feature['name'] == 'tamper' and state_access):
            alias = self._generate_alias(feature, 'tamper')
            self._add_device(alias, feature, ContactSensor)
            return

        if (feature['name'] == 'consumer_connected' and state_access):
            alias = self._generate_alias(feature, 'consmr')
            self._add_device(alias, feature, ContactSensor, ' (Consumer Connected)')
            return

        if (feature['name'] == 'running' and state_access):
            alias = self._generate_alias(feature, 'runng')
            self._add_device(alias, feature, ContactSensor, ' (Running)')
            return

        if (feature['name'] == 'state' and state_access and write_access):
            alias = self._generate_alias(feature, 'state')
            self._add_device(alias, feature, OnOffSwitch)
            return

        if (feature['name'] == 'temperature_setpoint_hold' and state_access and write_access):
            alias = self._generate_alias(feature, 'temphld')
            self._add_device(alias, feature, OnOffSwitch)
            return

        if (feature['name'] == 'led_disabled_night' and state_access and write_access):
            alias = self._generate_alias(feature, 'nled')
            self._add_device(alias, feature, OnOffSwitch)
            return

        if (feature['name'] == 'led_feedback' and state_access and write_access):
            alias = self._generate_alias(feature, 'ledfbk')
            self._add_device(alias, feature, OnOffSwitch)
            return

        if (feature['name'] == 'buzzer_feedback' and state_access and write_access):
            alias = self._generate_alias(feature, 'bzrfbk')
            self._add_device(alias, feature, OnOffSwitch)
            return

        if (feature['name'] == 'power_outage_memory' and state_access and write_access):
            alias = self._generate_alias(feature, 'pwrmem')
            self._add_device(alias, feature, OnOffSwitch, ' (Power Outage Memory)')
            return

        if (feature['name'] == 'auto_off' and state_access and write_access):
            alias = self._generate_alias(feature, 'autoff')
            self._add_device(alias, feature, OnOffSwitch, ' (Auto Off)')
            return

        if (feature['name'] == 'away_mode' and state_access and write_access):
            alias = self._generate_alias(feature, 'away')
            self._add_device(alias, feature, OnOffSwitch)
            return

        domoticz.debug(self.name + ': can not process binary item "' + feature['name'] + '"')
        domoticz.debug(json.dumps(feature))

    def add_numeric_device(self, feature):
        state_access = self._has_access(feature['access'], ACCESS_STATE)
        write_access = self._has_access(feature['access'], ACCESS_WRITE)

        # TODO: Use energy value for `power` feature
        if feature['name'] == 'energy':
            return

        if (feature['name'] == 'linkquality' and state_access):
            if domoticz.get_plugin_config('trackLinkQuality'):
                self._add_device('signal', feature, CustomSensor, ' (Link Quality)')
            return

        if feature['name'] == 'action_code' and state_access:
            alias = self._generate_alias(feature, 'accode')
            self._add_device(alias, feature, CustomSensor)
            return

        if feature['name'] == 'action_transaction' and state_access:
            alias = self._generate_alias(feature, 'actran')
            self._add_device(alias, feature, CustomSensor)
            return

        if feature['name'] == 'action_zone' and state_access:
            alias = self._generate_alias(feature, 'aczone')
            self._add_device(alias, feature, CustomSensor)
            return

        if (feature['name'] == 'battery' and state_access):
            if domoticz.get_plugin_config('useBatteryDevices'):
                self._add_device('btperc', feature, PercentageSensor, ' (Battery)')
            return

        if (feature['name'] == 'brightness' and state_access):
            alias = self._generate_alias(feature, 'light')
            self._add_device(alias, feature, DimmerSwitch)
            return

        if (feature['name'] == 'illuminance' and state_access):
            alias = self._generate_alias(feature, 'lux')
            self._add_device(alias, feature, LuxSensor, ' (Illuminance)')
            return

        if (feature['name'] == 'illuminance_lux' and state_access):
            alias = self._generate_alias(feature, 'lx')
            self._add_device(alias, feature, LuxSensor, ' (Illuminance Lux)')
            return

        if (feature['name'] == 'local_temperature' and state_access):
            alias = self._generate_alias(feature, 'ltemp')
            self._add_device(alias, feature, TemperatureSensor, ' (Local Temperature)')
            return
 
        if (feature['name'] == 'device_temperature' and state_access):
            alias = self._generate_alias(feature, 'ltemp')
            self._add_device(alias, feature, TemperatureSensor, ' (Device Temperature)')
            return

        if (feature['name'] == 'soil_moisture' and state_access):
            alias = self._generate_alias(feature, 'pres')
            self._add_device(alias, feature, PercentageSensor, ' (Soil Moisture)')
            return

        if feature['name'] == 'voltage' and state_access:
            if feature['description'] == 'Voltage of the battery in millivolts':
                alias = 'cell' # For migration from 0.2.x
            else:
                alias = self._generate_alias(feature, 'volt')

            self._add_device(alias, feature, VoltageSensor, ' (Voltage)')
            return

        if feature['name'] == 'co2' and feature['unit'] == 'ppm' and state_access:
            alias = self._generate_alias(feature, 'co2')
            self._add_device(alias, feature, CO2Sensor)
            return

        if feature['name'] == 'voc' and state_access:
            alias = self._generate_alias(feature, 'voc')
            self._add_device(alias, feature, CustomSensor)
            return

        if feature['name'] == 'formaldehyd' and state_access:
            alias = self._generate_alias(feature, 'fmdhd')
            self._add_device(alias, feature, CustomSensor)
            return

        if (feature['name'] == 'current' and state_access):
            alias = self._generate_alias(feature, 'ampere')
            self._add_device(alias, feature, CurrentSensor, ' (Current)')
            return

        if 'setpoint' in feature['name'] and 'unit' in feature and feature['unit'] == '°C' and write_access:
            alias = self._generate_alias(feature, 'spoint')
            self._add_device(alias, feature, SetPoint, ' (Setpoint)')
            return

        if feature['name'] == 'position':
            if write_access:
                alias = self._generate_alias(feature, 'level')
                self._add_device(alias, feature, LevelSwitch)
                return
            elif state_access and feature['unit'] == '%':
                alias = self._generate_alias(feature, 'level')
                self._add_device(alias, feature, PercentageSensor)
                return
            elif state_access:
                alias = self._generate_alias(feature, 'level')
                self._add_device(alias, feature, CustomSensor)
                return

        if feature['name'] == 'radioactive_events_per_minute' and state_access:
            alias = self._generate_alias(feature, 'repm')
            self._add_device(alias, feature, CustomSensor)
            return

        if feature['name'] == 'radiation_dose_per_hour' and state_access:
            alias = self._generate_alias(feature, 'reph')
            self._add_device(alias, feature, CustomSensor)
            return
        
        if (feature['name'] == 'sensors_count' and state_access):
            alias = self._generate_alias(feature, 'snscnt')
            self._add_device(alias, feature, CustomSensor)
            return

        if (feature['name'] == 'power_outage_count' and state_access):
            alias = self._generate_alias(feature, 'poutcnt')
            self._add_device(alias, feature, CustomSensor)
            return

        if (feature['name'] == 'water_consumed' and state_access):
            alias = self._generate_alias(feature, 'wtrcns')
            self._add_device(alias, feature, CustomSensor)
            return

        if (feature['name'] == 'last_valve_open_duration' and state_access):
            alias = self._generate_alias(feature, 'lvod')
            self._add_device(alias, feature, CustomSensor)
            return

        if (feature['name'] == 'color_temp_startup' and state_access):
            return

        if (feature['name'] == 'requested_brightness_level' and state_access):
            return

        if (feature['name'] == 'requested_brightness_percent' and state_access):
            return

        if (feature['name'] == 'pi_heating_demand' and state_access):
            alias = self._generate_alias(feature, 'phd')
            self._add_device(alias, feature, CustomSensor)
            return

        domoticz.debug(self.name + ': can not process numeric item "' + feature['name'] + '"')
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

        if feature['type'] == 'numeric' and 'setpoint' in feature['name'] and feature['unit'] == '°C' and write_access and command == 'Set Level':
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

        if feature['type'] == 'light' or feature['type'] == 'cover':
            state_feature = device.state_feature
            topic = self.name + '/' + ((state_feature['endpoint'] + '/set') if 'endpoint' in state_feature else 'set')

            return {
                'topic': topic,
                'payload': json.dumps(device.generate_command(command, level, color))
            }

        return None
