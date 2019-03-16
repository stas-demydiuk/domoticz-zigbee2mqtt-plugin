# Changelog

## master
- Add temperature sensor support for Xiaomi Mi power plug

New devices:
- IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, white spectrum, opal white

## 0.0.18
- Fix duplicate state in Domoticz log for On/Off switches
- Fix issue with reconnect after MQTT server restart (#84)
- Handle devices connect and removal from zigbee network

## 0.0.17
- Fix power consumption meter for Xiaomi Plugs

New devices:
- AduroSmart ERIA colors and white shades smart light bulb A19
- Airam LED OP A60 ZB 9W/827 E27
- Bitron Wireless motion detector
- Dresden Elektronik ZigBee Light Link wireless electronic ballast color temperature
- EcoSmart A19 RGB bulb
- EcoSmart A19 bright white bulb
- EcoSmart A19 soft white bulb
- GE ZigBee in-wall smart switch
- Gledopto Zigbee LED Driver
- Gledopto Smart 6W E27 RGB / CW LED bulb
- Gledopto Smart 12W E27 RGB / CW LED bulb
- Gledopto Zigbee LED controller WW/CW Dimmer
- Gledopto LED RGB + CCT downlight
- Gledopto Smart RGBW GU10
- Gledopto Smart RGBW GU10
- HEIMAN Door sensor
- HEIMAN Smoke detector
- Hive Active smart bulb white LED (B22)
- IKEA SURTE door light panel, dimmable, white spectrum (38x64 cm)
- Iris Motion and temperature sensor
- Müller Licht Tint LED bulb GU10/E14/E27 350/470/806 lumen, dimmable, color, opal white
- Müller Licht Tint LED bulb GU10/E14/E27 350/470/806 lumen, dimmable, opal white
- Nue ZigBee smart light controller
- OSRAM SMART+ Switch Mini
- Paul Neuhaus Q-INIGO LED ceiling light
- Philips Hue white ambiance BR30 flood light
- Philips Hue white ambiance Still
- Philips Hue white ambiance Aurelle round panel light
- Sengled Element Classic (BR30)
- Sengled Element downlight smart LED bulb
- Smart Home Pty RGBW Downlight
- Smart Home Pty Power plug
- SmartThings Motion sensor (2015 model)
- Sylvania Smart Home adjustable white A19 LED bulb
- Sylvania LIGHTIFY LED gardenspot mini RGB
- Trust Motion Sensor
- Trust Wireless contact sensor
- Xiaomi Aqara smart LED bulb
- iCasa Zigbee 3.0 Dimmer
- ilux Dimmable A60 E27 LED Bulb

## 0.0.16
- Added Domoticz devices to represent temperature + humidity for WSDCGQ11LM device
- Ability to manually specify Client ID for MQTT connection using plugin settings
- Suppress device update if no state change for boolean sensors

New devices:
- Calex LED A60 Zigbee GLS-lamp
- Climax Power plug
- Dresden Elektronik ZigBee Light Link wireless electronic ballast 
- Gledopto Zigbee LED controller RGB + CCT / RGBW / WWCW / Dimmer
- HEIMAN Door sensor
- Innr E27 Bulb RGBW
- Innr B22 Bulb RGBW
- Innr E14 Candle with white spectrum
- Iris Contact sensor
- JIAWEN Wireless Bulb E27 9W RGBW
- OSRAM Flex RGBW
- OSRAM Outdoor Flex RGBW
- OSRAM Smart+ Gardenpole RGBW
- OSRAM Smart+ outdoor wall lantern RGBW
- OSRAM Smart+ Ceiling TW
- OSRAM Smart+ Motion Sensor
- OSRAM Smart+ Spot GU10 Multicolor
- OSRAM Classic A60 RGBW
- OSRAM LIGHTIFY LED CLA60 E27 RGBW
- OSRAM LIGHTIFY Surface Light TW
- Paulmann SmartHome Zigbee LED-stripe
- Paulmann SmartHome Yourled RGB Controller
- Philips Hue Go
- Philips Hue white ambiance Aurelle Rectangle Panel Light
- Philips Hue white and color ambiance E26/E27/E14
- Philips Hue white and color ambiance GU10
- Philips Hue white and color ambiance LightStrip plus
- Philips Hue White and color ambiance Play Lightbar
- Philips Hue white and color ambiance BR30
- Philips Hue Motion Sensor
- Sengled Element Plus (A19)
- Sengled Element Plus Color (A19)
- SmartThings SmartSense multi sensor
- SmartThings SmartThings arrival sensor
- Sylvania LIGHTIFY LED RGBW A19
- Xiaomi MiJia Honeywell smoke detector

## 0.0.15
- Handle switch state change for PushOnButton
- Added Domoticz devices to represent Xiaomi Cube rotation angle and current side
- Added Domoticz devices to represent temperature, humidity and pressure in one device
- Added auth support for connection to MQTT server

New devices:
- Commercial Electric Matte White Recessed Retrofit Smart Led Downlight - 4 Inch
- IKEA TRADFRI LED bulb E12/E14 400 lumen, dimmable, white spectrum, opal white
- IKEA TRADFRI LED bulb GU10 400 lumen, dimmable, white spectrum
- IKEA TRADFRI LED bulb E26/E27 980 lumen, dimmable, white spectrum, opal white
- IKEA TRADFRI LED bulb E26/E27 950 lumen, dimmable, white spectrum, clear
- IKEA FLOALT LED light panel, dimmable, white spectrum (30x30 cm)
- IKEA FLOALT LED light panel, dimmable, white spectrum (30x90 cm)
- IKEA FLOALT LED light panel, dimmable, white spectrum (60x60 cm)
- Innr GU10 Spot 350 lm, dimmable, white spectrum
- OSRAM LIGHTIFY LED Classic A60 clear
- OSRAM SMART+ CLASSIC A 60 TW
- OSRAM LIGHTIFY LED A19 tunable white / Classic A60 TW
- OSRAM LIGHTIFY LED PAR16 50 GU10 tunable white
- OSRAM LIGHTIFY LED Classic B40 tunable white
- OSRAM LIGHTIFY Surface Light LED Tunable White
- Philips Hue Bloom
- Philips Hue white and color ambiance LightStrip
- Philips Hue Iris
- Philips Hue white ambiance E14
- Philips Hue white ambiance GU10
- Philips Hue white ambiance E26/E27
- Philips Hue Being
- Sylvania LIGHTIFY LED adjustable white RT 5/6
- Sylvania LIGHTIFY LED adjustable white BR30
- Sylvania Smart Home adjustable white MR16 LED bulb

## 0.0.14
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