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

### Belkin
- Belkin WeMo smart LED bulb

### Commercial Electric
- Commercial Electric Matte White Recessed Retrofit Smart Led Downlight - 4 Inch

### Dresden Elektronik
- Dresden Elektronik ZigBee Light Link wireless electronic ballast

### GE
- GE Link smart LED light bulb, BR30 soft white (2700K)
- GE ZigBee plug-in smart dimmer
- GE ZigBee in-wall smart dimmer

### Gledopto
- Gledopto Zigbee LED controller RGB + CCT / RGBW / WWCW / Dimmer 

### Hive
- Hive Active light dimmable

### Ikea
- IKEA TRADFRI LED bulb E26/E27 980 lumen, dimmable, white spectrum, opal white
- IKEA TRADFRI LED bulb E26/E27 950 lumen, dimmable, white spectrum, clear
- IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, opal white
- IKEA TRADFRI LED bulb GU10 400 lumen, dimmable, white spectrum
- IKEA TRADFRI LED bulb GU10 400 lumen, dimmable
- IKEA TRADFRI LED bulb E12/E14 400 lumen, dimmable, white spectrum, opal white
- IKEA TRADFRI LED bulb E26 1000 lumen, dimmable, opal white
- IKEA TRADFRI LED bulb E27 600 lumen, dimmable, color, opal white
- IKEA TRADFRI LED bulb E14 400 lumen, dimmable warm white, chandelier opal
- IKEA TRADFRI wireless dimmer
- IKEA TRADFRI driver for wireless control (10 watt)
- IKEA TRADFRI driver for wireless control (30 watt)
- IKEA FLOALT LED light panel, dimmable, white spectrum (30x30 cm)
- IKEA FLOALT LED light panel, dimmable, white spectrum (60x60 cm)
- IKEA FLOALT LED light panel, dimmable, white spectrum (30x90 cm)
- IKEA TRADFRI control outlet

### Innr
- Innr E27 Bulb
- Innr E27 Bulb warm dimming
- Innr E27 Bulb RGBW
- Innr GU10 Spot
- Innr GU10 Spot 350 lm, dimmable, white spectrum
- Innr E14 Candle
- Innr B22 Bulb dimmable
- Innr B22 Bulb RGBW
- Innr Puck Light
- Innr Strip Light
- Innr Under Cabinet Light
- Innr Spot narrow
- Innr Spot wide
- Innr Spot Flex narrow
- Innr Spot Flex medium
- Innr Spot Flex wide

### Iris
- Iris Smart plug

### JIAWEN
- JIAWEN Wireless Bulb E27 9W RGBW

### Ksentry
- Ksentry Electronics Zigbee OnOff Controller

### Nanoleaf
- Nanoleaf Ivy smart bulb

### Nue
- Nue ZigBee one gang smart switch

### OSRAM
- OSRAM LIGHTIFY LED A19 tunable white / Classic A60 TW 
- OSRAM LIGHTIFY LED PAR16 50 GU10 tunable white
- OSRAM LIGHTIFY LED Classic B40 tunable white
- OSRAM LIGHTIFY LED Classic A60 clear
- OSRAM LIGHTIFY LED CLA60 E27 RGBW
- OSRAM LIGHTIFY Surface Light LED Tunable White
- OSRAM LIGHTIFY Surface Light TW
- OSRAM Smart+ Candle E14 Dimmable White
- OSRAM Smart+ Ceiling TW
- OSRAM Smart+ Classic A 60 TW
- OSRAM Smart+ Gardenpole RGBW
- OSRAM Smart+ Motion Sensor
- OSRAM Smart+ Outdoor Wall Lantern RGBW
- OSRAM Smart+ Plug
- OSRAM Smart+ Spot GU10 Multicolor
- OSRAM Flex RGBW
- OSRAM Outdoor Flex RGBW
- OSRAM Classic A60 RGBW

### Philips
- Philips Hue dimmer switch
- Philips Hue Go
- Philips Hue Lux A19 bulb E27
- Philips Hue white A60 bulb E27
- Philips Hue White Single bulb B22
- Philips Hue white ambiance E14
- Philips Hue white ambiance GU10
- Philips Hue white ambiance E26/E27
- Philips Hue white and color ambiance BR30
- Philips Hue white and color ambiance GU10
- Philips Hue white and color ambiance E26/E27/E14
- Philips Hue white and color ambiance LightStrip plus
- Philips Hue White and color ambiance Play Lightbar
- Philips Hue Being
- Philips Hue Motion Sensor

### Sengled
- Sengled Element Classic (A19)
- Sengled Element Classic (A60)
- Sengled Element Plus Color (A19)
- Sengled Element Touch (A19)

### SmartThings
- SmartThings SmartSense multi sensor
- SmartThings Arrival sensor

### Sylvania
- Sylvania LIGHTIFY LED adjustable white RT 5/6
- Sylvania LIGHTIFY LED adjustable white BR30
- Sylvania LIGHTIFY LED RGBW A19
- Sylvania LIGHTIFY LED soft white dimmable A19
- Sylvania LIGHTIFY LED soft white dimmable A19
- Sylvania SMART+ Smart Plug
- Sylvania Smart Home adjustable white MR16 LED bulb

### Trust
- Trust Smart Dimmable LED Bulb

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
- Xiaomi MiJia Honeywell smoke detector
- Xiaomi MiJia human body movement sensor
- Xiaomi MiJia temperature & humidity sensor
- Xiaomi MiJia wireless switch
- Xiaomi Mi smart home cube
- Xiaomi Mi power plug ZigBee

### Other
- Custom devices (DiY) DNCKAT single key wired wall light switch
- Paulmann SmartHome Zigbee LED-stripe

If your device is not listed here but [zigbee2mqtt supports](https://github.com/Koenkk/zigbee2mqtt/wiki/Supported-devices) it, support can be added (fairly) easy by creating device adapter.
