# Zigbee2MQTT - Domoticz Python Plugin
Python plugin for Domoticz to add integration with [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) project

## Prerequisites

- Setup and run zigbee2mqtt server (https://www.zigbee2mqtt.io).
- Make sure that your Domoticz supports Python plugins (https://www.domoticz.com/wiki/Using_Python_plugins)


## Installation

1. Clone repository into your domoticz plugins folder
```
cd domoticz/plugins
git clone https://github.com/stas-demydiuk/domoticz-zigbee2mqtt-plugin.git zigbee2mqtt
```
2. Restart domoticz
3. Make sure that "Accept new Hardware Devices" is enabled in Domoticz settings
4. Go to "Hardware" page and add new item with type "Zigbee2MQTT"
5. Set your MQTT server address and port to plugin settings

Once plugin receive device list from zigbee2mqtt server it will create appropriate domoticz devices. You will find these devices on `Setup -> Devices` page.

## Plugin update

1. Go to plugin folder and pull new version
```
cd domoticz/plugins/zigbee2mqtt
git pull
```
2. Restart domoticz

## Zigbee groups support

Plugin supports [zigbee groups](https://www.zigbee2mqtt.io/information/groups.html). It is impossible to automatically identify what device should represent the group (OnOff switch, dimmer, etc.), so plugin relies on suffixes in zigbee group name. Currently following suffixes are supported:

| Suffix  | Device Type                           | Example        |
|---------|---------------------------------------|----------------|
| _dimmer | Dimmer Switch                         | mygroup_dimmer |
| _ct     | Dimmer Switch with Color Temperature  | mygroup_ct     |

if no suffix will be found then On/Off switch will be created by default

## Supported devices

### AduroSmart
- AduroSmart ERIA colors and white shades smart light bulb A19

### Airam
- Airam LED OP A60 ZB 9W/827 E27

### Anchor
- Anchor Vetaar smart plug

### Belkin
- Belkin WeMo smart LED bulb

### Bitron
- Bitron Wireless motion detector
- Bitron Wireless smart plug
- Bitron Wireless wall thermostat with relay

### Blitzwolf
- Blitzwolf BW-IS4 Temperature & humidity sensor with display

### Bosch
- Bosch Motion sensor
- Bosch Wireless motion detector

### Calex
- Calex LED A60 Zigbee GLS-lamp

### Climax
- Climax Power plug

### Commercial Electric
- Commercial Electric Matte White Recessed Retrofit Smart Led Downlight - 4 Inch

### CR Smart Home
- CR Smart Home Valve control
- CR Smart Home Motion sensor
- CR Smart Home Door sensor
- CR Smart Home Smoke sensor
- CR Smart Home Socket
- CR Smart Home Water leak detector

### Dresden Elektronik
- Dresden Elektronik ZigBee Light Link wireless electronic ballast
- Dresden Elektronik ZigBee Light Link wireless electronic ballast color temperature

### EcoSmart
- EcoSmart A19 RGB bulb
- EcoSmart A19 bright white bulb
- EcoSmart A19 soft white bulb

### ELKO
- Elko ESH RS16 316GLED dimmer RF PH. ZigBee in-wall smart dimmer

### GE
- GE Link smart LED light bulb, BR30 soft white (2700K)
- GE ZigBee plug-in smart dimmer
- GE ZigBee plug-in smart switch
- GE ZigBee in-wall smart dimmer
- GE ZigBee in-wall smart switch

### Gira
- Gira ZigBee Light Link wall transmitter

### Gledopto
- Gledopto LED RGB + CCT downlight
- Gledopto Smart 12W E27 RGB / CW LED bulb
- Gledopto Smart 6W E27 RGB / CW LED bulb
- Gledopto Smart RGB+CCT GU10
- Gledopto Smart RGBW GU10
- Gledopto Smart Wnite GU10
- Gledopto Soposh dual white and color
- Gledopto Zigbee 10W floodlight RGB CCT
- Gledopto Zigbee LED Driver
- Gledopto Zigbee LED controller RGB + CCT / RGBW / WWCW / Dimmer 
- Gledopto Zigbee LED controller RGB + CCT or RGBW
- Gledopto Zigbee LED controller RGB + CCT plus model
- Gledopto Zigbee LED controller RGBW plus model    
- Gledopto Zigbee LED controller WW/CW Dimmer
- Gledopto Zigbee LED controller dimmer
- Gledopto Zigbee ON/OFF Wall Switch
- Gledopto Zigbee USB mini LED controller RGB + CCT

### HEIMAN
- HEIMAN Door sensor
- HEIMAN Smoke detector
- HEIMAN Water leakage sensor
- HEIMANN Carbon monoxide sensor

### Hive
- Hive Active smart bulb white LED (E27)
- Hive Active smart bulb white LED (B22)

### Ikea
- IKEA GUNNARP LED light panel, dimmable, white spectrum (40x40 cm)
- IKEA SYMFONISK sound controller
- IKEA TRADFRI LED bulb E26/E27 980 lumen, dimmable, white spectrum, opal white
- IKEA TRADFRI LED bulb E26/E27 950 lumen, dimmable, white spectrum, clear
- IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, opal white
- IKEA TRADFRI LED bulb GU10 400 lumen, dimmable, white spectrum
- IKEA TRADFRI LED bulb GU10 400 lumen, dimmable
- IKEA TRADFRI LED bulb E12/E14 400 lumen, dimmable, white spectrum, opal white
- IKEA TRADFRI LED bulb E12 600 lumen, dimmable, white spectrum, opal white
- IKEA TRADFRI LED bulb E26 1000 lumen, dimmable, opal white
- IKEA TRADFRI LED bulb E26/E27 806 lumen, dimmable, warm white
- IKEA TRADFRI LED bulb E27 600 lumen, dimmable, color, opal white
- IKEA TRADFRI LED bulb E27 806 lumen, dimmable, white spectrum, clear
- IKEA TRADFRI LED bulb E27 1000 lumen, dimmable, white spectrum, opal white
- IKEA TRADFRI LED bulb E14 400 lumen, dimmable warm white, chandelier opal
- IKEA TRADFRI LED bulb E14 600 lumen, dimmable, white spectrum, opal white
- IKEA TRADFRI wireless dimmer
- IKEA TRADFRI remote control
- IKEA TRADFRI driver for wireless control (10 watt)
- IKEA TRADFRI driver for wireless control (30 watt)
- IKEA TRADFRI control outlet
- IKEA TRADFRI ON/OFF switch
- IKEA TRADFRI motion sensor
- IKEA TRADFRI signal repeater
- IKEA FLOALT LED light panel, dimmable, white spectrum (30x30 cm)
- IKEA FLOALT LED light panel, dimmable, white spectrum (60x60 cm)
- IKEA FLOALT LED light panel, dimmable, white spectrum (30x90 cm)
- IKEA SURTE door light panel, dimmable, white spectrum (38x64 cm)
- IKEA LEPTITER Recessed spot light
- IKEA FYRTUR block-out roller blind

### Itead
- ITEAD SONOFF ZigBee DIY Smart Switch

### Immax
- Immax LED E14/230V C35 5W TB 440LM ZIGBEE DIM 

### Innr
- Innr Color Flex LED strip
- Innr E27 Bulb
- Innr E27 Bulb warm dimming
- Innr E27 Bulb filament clea
- Innr E27 Bulb RGBW
- Innr E27 filament bulb dimmable
- Innr E27 Smart bulb tunable white
- Innr GU10 Spot
- Innr GU10 Spot 350 lm, dimmable, white spectrum
- Innr E14 Bulb RGBW
- Innr E14 Candle
- Innr E14 Candle with white spectrum
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
- Iris Contact sensor
- Iris Motion and temperature sensor
- Iris Smart plug

### JIAWEN
- JIAWEN Wireless Bulb E27 9W RGBW

### Konke
- Konke Multi-function button
- Konke Temperature and humidity sensor
- Konke Motion sensor
- Konke Contact sensor
- Konke Water detector

### Ksentry
- Ksentry Electronics Zigbee OnOff Controller

### Ligan
- Lingan Zigbee OnOff Controller

### Livolo
- Livolo Switch TI0001

### Müller Licht
- Müller Licht Tint LED bulb GU10/E14/E27 350/470/806 lumen, dimmable, color, opal white
- Müller Licht Tint LED bulb GU10/E14/E27 350/470/806 lumen, dimmable, opal white
- Müller Licht Tint smart switch

### Nanoleaf
- Nanoleaf Ivy smart bulb

### Netvox
- Netvox Power socket with power consumption monitoring

### Nue
- Nue ZigBee one gang smart switch
- Nue ZigBee smart light controller

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
- OSRAM SMART+ spot GU5.3 tunable white
- OSRAM Smart+ Spot GU10 Multicolor
- OSRAM Smart+ Switch Mini
- OSRAM Flex RGBW
- OSRAM Outdoor Flex RGBW
- OSRAM Classic A60 RGBW

### Oujiabao
- Oujiabao Gas and carbon monoxide alarm

### Paul Neuhaus
- Paul Neuhaus Q-INIGO LED ceiling light
- Paul Neuhaus Q-FLAG LED Panel, Smart-Home RGBW 

### Paulmann
- Paulmann SmartHome Zigbee LED-stripe
- Paulmann SmartHome Yourled RGB Controller

### Philips
- Philips Hue Being
- Philips Hue Cher ceiling light
- Philips Hue Filament Standard A60/E27 bluetooth
- Philips Hue Fillament Bulb G93
- Philips Hue Fuzo outdoor wall light
- Philips Hue Go
- Philips Hue Go with Bluetooth
- Philips Hue Lily outdoor spot light
- Philips Hue Lux A19 bulb E27
- Philips Hue Sana
- Philips Hue Struana
- Philips Hue Welcome white flood light
- Philips Hue dimmer switch
- Philips Hue motion outdoor sensor
- Philips Hue motion sensor
- Philips Hue smart plug - EU
- Philips Hue smart plug bluetooth
- Philips Hue white A60 bulb E27
- Philips Hue white A60 bulb E27 bluetooth
- Philips Hue white E14
- Philips Hue white GU10
- Philips Hue white GU10 bluetooth
- Philips Hue white PAR38 outdoor
- Philips Hue white Single bulb B22
- Philips Hue white ambiance Adore light
- Philips Hue white ambiance Aurelle Rectangle Panel Light
- Philips Hue white ambiance Aurelle rectangle panel light
- Philips Hue white ambiance Aurelle round panel light
- Philips Hue white ambiance Aurelle square panel light
- Philips Hue white ambiance BR30 flood light
- Philips Hue white ambiance E14
- Philips Hue white ambiance E26
- Philips Hue white ambiance E26 with Bluetooth
- Philips Hue white ambiance E26/E27
- Philips Hue white ambiance E27 with Bluetooth
- Philips Hue white ambiance GU10
- Philips Hue white ambiance GU10 with Bluetooth
- Philips Hue white ambiance Still
- Philips Hue white ambiance suspension Fair
- Philips Hue white and color ambiance BR30
- Philips Hue white and color ambiance BR30 with bluetooth
- Philips Hue white and color ambiance E26/E27
- Philips Hue white and color ambiance E26/E27/E14
- Philips Hue white and color ambiance Flourish ceiling light
- Philips Hue white and color ambiance GU10
- Philips Hue white and color ambiance LightStrip outdoor
- Philips Hue white and color ambiance LightStrip plus
- Philips Hue white and color ambiance Play Lightbar
- Philips Hue white filament Edison E27 LED
- Philips LivingColors Aura
- Philips Phoenix light

### ROBB
- ROBB ZigBee AC phase-cut dimmer
- ROBB ZigBee AC phase-cut rotary dimmer

### Sengled
- Sengled Element Classic (A19)
- Sengled Element Classic (A60)
- Sengled Element Classic (BR30)
- Sengled Element downlight smart LED bulb
- Sengled Element Plus (A19)
- Sengled Element Plus Color (A19)
- Sengled Element Touch (A19)

### Smart Home Pty
- Smart Home Pty RGBW Downlight
- Smart Home Pty Power plug

### SmartThings
- SmartThings Arrival sensor
- SmartThings Door sensor
- SmartThings Motion sensor (2014, 2015, 2016, 2018 models)
- SmartThings Multi sensor (2015, 2016, 2018 models)
- SmartThings Multipurpose sensor (2015, 2016, 2018 models)
- SmartThings Outlet
- SmartThings Outlet

### Stelpro
- Stelpro Built-in electronic thermostat

### Swann
- Swann Key fob remote
- Swann Window/door sensor

### Sylvania
- Sylvania LIGHTIFY LED RGBW A19
- Sylvania LIGHTIFY LED RGBW BR30
- Sylvania LIGHTIFY LED adjustable white BR30
- Sylvania LIGHTIFY LED adjustable white RT 5/6
- Sylvania LIGHTIFY LED gardenspot mini RGB
- Sylvania LIGHTIFY LED soft white dimmable A19
- Sylvania LIGHTIFY LED soft white dimmable A19
- Sylvania SMART+ Smart Plug
- Sylvania Smart Home adjustable white A19 LED bulb
- Sylvania Smart Home adjustable white MR16 LED bulb

### Trust
- Trust Remote control
- Trust Smart Dimmable LED Bulb
- Trust Smart Tunable LED bulb
- Trust Motion Sensor
- Trust Water leakage detector
- Trust Wireless contact sensor

### TUYATEC
- TUYATEC PIR sensor
- TUYATEC Temperature & humidity sensor
- TUYATEC Smart light switch - 1 gang without neutral wire
- TUYATEC Zigbee smart dimmer
- TUYATEC Temperature & humidity sensor with display

### Xiaomi

- Xiaomi Aqara Opple 4-button switch
- Xiaomi Aqara Opple 6-button switch
- Xiaomi Aqara curtain motor
- Xiaomi Aqara door & window contact sensor
- Xiaomi Aqara double key wired wall switch
- Xiaomi Aqara double key wireless wall switch
- Xiaomi Aqara human body movement and illuminance sensor
- Xiaomi Aqara single key wired wall switch
- Xiaomi Aqara single key wireless wall switch
- Xiaomi Aqara smart LED bulb
- Xiaomi Aqara socket Zigbee
- Xiaomi Aqara temperature, humidity and pressure sensor
- Xiaomi Aqara two-way control module
- Xiaomi Aqara vibration sensor
- Xiaomi Aqara water leak sensor
- Xiaomi Aqara wireless switch (WXKG11LM)
- Xiaomi Aqara wireless switch with gyroscope (WXKG12LM)
- Xiaomi Mi power plug ZigBee
- Xiaomi Mi power plug ZigBee EU
- Xiaomi Mi smart home cube
- Xiaomi MiJia Honeywell smoke detector
- Xiaomi MiJia door & window contact sensor
- Xiaomi MiJia gas leak detector
- Xiaomi MiJia light intensity sensor
- Xiaomi MiJia human body movement sensor
- Xiaomi MiJia temperature & humidity sensor
- Xiaomi MiJia wireless switch

### Weiser
- Weiser SmartCode 10
- Weiser SmartCode 10 Touch

### eWeLink
- eWeLink Zigbee smart plug

### iCasa
- iCasa Zigbee 3.0 Dimmer
- iCasa Zigbee 3.0 Switch

### ilux
- ilux Dimmable A60 E27 LED Bulb

### Eurotronic
- Eurotronic SPZB0001 thermostat

### Zemismart
- Zemismart ZM-CSW002-D 2 gang switch
- Zemismart ZM-L03E-Z 3 gang with neutral wire switch
- Zemismart RGB LED downlight
- Zemismart Curtain/roller blind switch

### Other
- Custom devices (DiY) DNCKAT single key wired wall light switch
- Custom devices (DiY) ZigUP
- DIYRuZ DIYRuZ_magnet

If your device is not listed here but [zigbee2mqtt supports](https://koenkk.github.io/zigbee2mqtt/information/supported_devices.html) it, support can be added (fairly) easy by creating device adapter.
