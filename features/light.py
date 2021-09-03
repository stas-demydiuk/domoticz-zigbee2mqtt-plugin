import domoticz
import json
from feature_utils import get_feature, generate_alias
from devices.light.on_off import OnOffLight
from devices.light.dimmer import DimmerLight
from devices.light.ct import CTLight
from devices.light.rgb import RGBLight
from devices.light.rgbw import RGBWLight

class LightFeatureProcesor():
    def __init__(self, adapter):
        self.adapter = adapter

    def _add_light_feature(self, feature):
        light_features = feature['features']
        
        state = get_feature(light_features, 'state')
        brightness = get_feature(light_features, 'brightness')
        color_temp = get_feature(light_features, 'color_temp')
        color = get_feature(light_features, 'color_xy')
        
        alias = generate_alias(state, 'light')

        if state and brightness and color_temp and color:
            device = RGBWLight(alias)
            device.set_state_feature(state)
            device.set_brightness_feature(brightness)
            device.set_color_temp_feature(color_temp)
            device.set_color_feature(color)
        elif state and brightness and color:
            device = RGBLight(alias)
            device.set_state_feature(state)
            device.set_brightness_feature(brightness)
            device.set_color_feature(color)
        elif state and brightness and color_temp:
            device = CTLight(alias)
            device.set_state_feature(state)
            device.set_brightness_feature(brightness)
            device.set_color_temp_feature(color_temp)
        elif state and brightness:
            device = DimmerLight(alias)
            device.set_state_feature(state)
            device.set_brightness_feature(brightness)
        elif state:
            device = OnOffLight('switch')
            device.set_state_feature(state)
        else:
            domoticz.error(self.adapter.name + ': can not find appropriate device type to handle light feature')
            domoticz.debug(json.dumps(feature))

        if device:
            device.feature = feature
            
        # Add rest light features
        for item in light_features:
            name = item['name']
            
            if name != 'state' and name != 'brightness' and name != 'color_temp' and name != 'color_xy':
                self.adapter._add_feature(item)

        return device

    def register(self, features):
        devices = []

        for item in features:
            if item['type'] == 'light':
                devices.append(self._add_light_feature(item))

        return devices


