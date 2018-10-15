# Changelog

## 0.0.5
Breaking changes: 
- Avoid using Domoticz Device Options to store device internal data
- Start consuming DeviceID to store ieee_address and alias

New features:
- `include_device_information` flag in not required anymore in zigbee2mqtt configuration

## 0.0.4
New features:
- Added IKEA TRADFRI wireless dimmer support

## 0.0.3
Breaking changes: 
- Added ability to set Zigbee2Mqtt topic in plugin settings
    Requires to manually set topic for those who used previous plugin version (default topic is zigbee2mqtt)

New features:
- Added Xiaomi Aqara human body movement and illuminance sensor 

## 0.0.2
New features:
- Added Xiaomi Aqara door & window contact sensor support
- Added check if MQTT message from zigbee2mqtt contains device information