import domoticz
from feature_utils import get_feature, generate_alias
from devices.switch.blind_percentages_switch import BlindSwitch


class CoverFeatureProcessor():
    def __init__(self, adapter):
        self.adapter = adapter

    def _add_cover_feature(self, feature):
        cover_features = feature['features']
        state = get_feature(cover_features, 'state')
        position = get_feature(cover_features, 'position')
        device = None

        if state and position:
            alias = generate_alias(state, 'dimmer')
            device = BlindSwitch(domoticz.get_devices(), alias, position['property'], ' (Position)')
            device.set_state_feature(state)
            device.set_position_feature(position)
            device.feature = feature

        # Add rest sub features
        for item in cover_features:
            name = item['name']
            
            if name != 'state' and name != 'position':
                self.adapter._add_feature(item)

        return device
    
    def register(self, features):
        devices = []

        for item in features:
            if item['type'] == 'cover':
                devices.append(self._add_cover_feature(item))

        return devices