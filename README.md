# Zigbee2MQTT - Domoticz Python Plugin
Python plugin for Domoticz to add integration with [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) project

## Prerequisites

Setup and run zigbee2mqtt server (https://github.com/Koenkk/zigbee2mqtt/wiki).

## Installation

1. Clone repository into your domoticz plugins folder
```
cd domoticz/plugins
git clone https://github.com/stas-demydiuk/domoticz-zigbee2mqtt-plugin.git zigbee2mqtt
```
2. Restart domoticz
3. Go to "Hardware" page and add new item with type "Zigbee2MQTT"
4. Set your MQTT server address and port to plugin settings

Once plugin receive any message from zigbee2mqtt server it will try to create appropriate device.

## Plugin update

1. Stop domoticz
2. Go to plugin folder and pull new version
```
cd domoticz/plugins/zigbee2mqtt
git pull
```
3. Start domoticz

## Supported devices

### GE
- GE Link smart LED light bulb, BR30 soft white (2700K)
- GE ZigBee plug-in smart dimmer
- GE ZigBee in-wall smart dimmer

### Ikea
- IKEA TRADFRI control outlet
- IKEA TRADFRI wireless dimmer
- IKEA TRADFRI driver for wireless control (10 watt)
- IKEA TRADFRI driver for wireless control (30 watt)
- IKEA TRADFRI LED bulb E26 1000 lumen, dimmable, opal white
- IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, opal white
- IKEA TRADFRI LED bulb E27 600 lumen, dimmable, color, opal white
- IKEA TRADFRI LED bulb E14 400 lumen, dimmable warm white, chandelier opal
- IKEA TRADFRI LED bulb GU10 400 lumen, dimmable

### Innr
- Innr E27 Bulb
- Innr E27 Bulb warm dimming
- Innr GU10 Spot
- Innr E14 Candle
- Innr B22 Bulb dimmable
- Innr Puck Light
- Innr Strip Light
- Innr Under Cabinet Light
- Innr Spot narrow
- Innr Spot wide
- Innr Spot Flex narrow
- Innr Spot Flex medium
- Innr Spot Flex wide

### OSRAM
- OSRAM Smart+ plug
- OSRAM LIGHTIFY LED Classic A60 clear

### Philips
- Philips Hue dimmer switch
- Philips Hue Lux A19 bulb E27
- Philips Hue white A60 bulb E27
- Philips Hue White Single bulb B22

### Sengled
- Sengled Element Classic (A19)
- Sengled Element Classic (A60)
- Sengled Element Touch (A19)

### Sylvania
- Sylvania LIGHTIFY LED soft white dimmable A19
- Sylvania LIGHTIFY LED soft white dimmable A19
- Sylvania SMART+ Smart Plug

### Xiaomi

- Xiaomi Aqara door & window contact sensor
- Xiaomi Aqara double key wired wall switch
- Xiaomi Aqara double key wireless wall switch
- Xiaomi Aqara human body movement and illuminance sensor
- Xiaomi Aqara single key wired wall switch
- Xiaomi Aqara single key wireless wall switch
- Xiaomi Aqara socket Zigbee
- Xiaomi Aqara temperature, humidity and pressure sensor
- Xiaomi Aqara vibration sensor
- Xiaomi Aqara water leak sensor
- Xiaomi Aqara wireless switch (WXKG11LM)
- Xiaomi Aqara wireless switch with gyroscope (WXKG12LM)
- Xiaomi MiJia door & window contact sensor
- Xiaomi MiJia human body movement sensor
- Xiaomi MiJia temperature & humidity sensor
- Xiaomi MiJia wireless switch
- Xiaomi Mi smart home cube
- Xiaomi Mi power plug ZigBee

### Other
- Belkin WeMo smart LED bulb
- Custom devices (DiY) DNCKAT single key wired wall light switch
- Hive Active light dimmable
- Iris Smart plug
- Ksentry Electronics Zigbee OnOff Controller
- Nanoleaf Ivy smart bulb
- Nue ZigBee one gang smart switch
- Paulmann SmartHome Zigbee LED-stripe
- Trust Smart Dimmable LED Bulb

If your device is not listed here but [zigbee2mqtt supports](https://github.com/Koenkk/zigbee2mqtt/wiki/Supported-devices) it, support can be added (fairly) easy by creating device adapter.
