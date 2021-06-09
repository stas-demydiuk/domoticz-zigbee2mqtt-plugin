import domoticz
from feature_utils import get_feature, generate_alias
from devices.sensor.humidity import HumiditySensor
from devices.sensor.pressure import PressureSensor
from devices.sensor.temperature import TemperatureSensor
from devices.temperature_humidity_sensor import TemperatureHumiditySensor
from devices.temperature_humidity_barometer_sensor import TemperatureHumidityBarometerSensor

class TempHumPressureFeatureProcessor():
    def register(self, features):
        devices = []

        temp = get_feature(features, 'temperature')
        humidity = get_feature(features, 'humidity')
        pressure = get_feature(features, 'pressure')

        if temp:
            alias = generate_alias(temp, 'temp')
            device = TemperatureSensor(domoticz.get_devices(), alias, temp['property'], ' (Temperature)')
            device.feature = temp
            devices.append(device)

        if humidity:
            alias = generate_alias(humidity, 'hum')
            device = HumiditySensor(domoticz.get_devices(), alias, humidity['property'], ' (Humidity)')
            device.feature = humidity
            devices.append(device)

        if pressure:
            alias = generate_alias(pressure, 'pres')
            device = PressureSensor(domoticz.get_devices(), alias, pressure['property'], ' (Pressure)')
            device.feature = pressure
            devices.append(device)
            
        if temp and humidity:
            device = TemperatureHumiditySensor(domoticz.get_devices(), 'all', 'temp+hum', ' (Temperature + Humidity)')
            device.set_temp_feature(temp)
            device.set_humidity_feature(humidity)
            device.feature = temp
            devices.append(device)

        if temp and humidity and pressure:
            device = TemperatureHumidityBarometerSensor(domoticz.get_devices(), 'thb', 'temp+hum+bar', ' (Temperature + Humidity + Barometer)')
            device.set_temp_feature(temp)
            device.set_humidity_feature(humidity)
            device.set_pressure_feature(pressure)
            device.feature = temp
            devices.append(device)

        return devices