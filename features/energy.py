import domoticz
from feature_utils import get_feature, generate_alias
from devices.sensor.kwh import KwhSensor


class EnergyFeatureProcessor():
    def register(self, features):
        devices = []
        power = get_feature(features, 'power')
        energy = get_feature(features, 'energy')
        device = None

        if power and energy:
            device = KwhSensor('power', [power['property'], energy['property']], ' (Power)')
        elif power:
            device = KwhSensor('power', [power['property']], ' (Power)')

        if device:
            device.feature = power
            devices.append(device)

        return devices