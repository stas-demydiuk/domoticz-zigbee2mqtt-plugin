# Changelog

## master
- Added new devices in Domoticz to handle link quality and batery level for devices in zigbee network

New devices:
- Belkin WeMo smart LED bulb
- Custom devices (DiY) DNCKAT single key wired wall light switch
- GE Link smart LED light bulb, BR30 soft white (2700K)
- GE ZigBee plug-in smart dimmer
- GE ZigBee in-wall smart dimmer
- Hive Active light dimmable
- Iris Smart plug
- Ksentry Electronics Zigbee OnOff Controller
- IKEA TRADFRI control outlet
- IKEA TRADFRI driver for wireless control (10 watt)
- IKEA TRADFRI driver for wireless control (30 watt)
- Innr bulbs
- Nanoleaf Ivy smart bulb
- Nue ZigBee one gang smart switch
- OSRAM Smart+ plug
- OSRAM LIGHTIFY LED Classic A60 clear
- Paulmann SmartHome Zigbee LED-stripe
- Philips Hue dimmer switch
- Philips Hue Lux A19 bulb E27
- Philips Hue white A60 bulb E27
- Philips Hue White Single bulb B22
- Sengled Element Classic (A19)
- Sengled Element Classic (A60)
- Sengled Element Touch (A19)
- Sylvania LIGHTIFY LED soft white dimmable A19
- Sylvania LIGHTIFY LED soft white dimmable A19
- Sylvania SMART+ Smart Plug
- Trust Smart Dimmable LED Bulb
- Xiaomi Aqara single key wired wall switch

## 0.0.13
- Added Xiaomi Aqara vibration sensor support
- Added IKEA TRADFRI LED bulb E26 1000 lumen, dimmable, opal white support
- Added IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, opal white support
- Added IKEA TRADFRI LED bulb E14 400 lumen, dimmable warm white, chandelier opal support
- Added IKEA TRADFRI LED bulb GU10 400 lumen, dimmable support
- Fix issue with levels for different models of Xiaomi Aqara wireless switch (WXKG11LM)
- Fix issue with creating PushOnButton
- Fix issue with handling MQTT messages for Nanoleaf NL08-0800 Bulb

## 0.0.12
New features:
 - Added support for IKEA Tradfri LED1624G9 (Thanks to @JanJaapKo)
 - Added support for Nanoleaf Smart Ivy bulb (Thanks to @JanJaapKo)
 - Create devices in Domoticz after plugin receive device list from zigbee gateway

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