# Changelog

## 0.0.11
- Fix error when receive device without model data (#20)
- Fix WXKG12LM message convertion error (#21)

## 0.0.10
New features:
- Added Xiaomi Aqara wireless switch with gyroscope (WXKG12LM) support

## 0.0.9
New features:
- Added Xiaomi Aqara wireless switch (WXKG11LM) support
- Added Xiaomi Aqara single key wireless wall switch (WXKG03LM) support

## 0.0.8
- Fix device link quality processing (#5)
- Fix falsy device updates (#14)

## 0.0.7
- Added ability to change Xiaomi Switch, Wireless Wall Switch and Cube device states from Domoticz

## 0.0.6
New features:
- Added Xiaomi Aqara socket Zigbee support
- Added Xiaomi MiJia temperature & humidity sensor support

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