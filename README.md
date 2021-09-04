# Zigbee2MQTT - Domoticz Python Plugin
Python plugin for Domoticz to add integration with [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) project

![image](https://user-images.githubusercontent.com/2734836/79760084-363b2e00-8328-11ea-994f-32b7b58ea6be.png)

## Prerequisites

- Setup and run zigbee2mqtt 1.17+ server (https://www.zigbee2mqtt.io).
- Make sure that your Domoticz supports Python plugins (https://www.domoticz.com/wiki/Using_Python_plugins)

** Plugin now uses [Extended Domoticz Plugins Framework](https://www.domoticz.com/wiki/Developing_a_Python_plugin#Extended_Plugin_Framework) which is available only in latest Domoticz betas

## Installation

You can use [Plugins Manager](https://github.com/stas-demydiuk/domoticz-plugins-manager) for automatic installation or follow manual steps:

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
| _rgb    | RGB Switch                            | mygroup_rgb    |
| _rgbw   | RGBW Switch                           | mygroup_rgbw   |

if no suffix will be found then On/Off switch will be created by default

## Configuration

Plugin uses internal configuration to associate physical zigbee devices to logical ones in Domoticz. Configuration is a plain JSON object with the following structure:

```ts
{
    "aliases": Alias[]
}
```

where `Alias` type is used to associate single zigbee device feature to Domoticz logical device and viceversa. It has the following structure

```ts
{
    "domoticz": {
        "device_id": String     // Domoticz Device ID (not idx) in Domoticz
        "legacy_alias": String  // Alias, legacy key that was used in zigbee2mqtt plugin <= 3.0, required to support logical devices that were created before
        "unit": Number          // Domoticz Device Unit
    },
    "zigbee": {
        "adress": String        // Zigbee IEEE Address
        "endpoint": String      // Zigbee endpoint (for devices that have multiple ones like switches with several buttons)
        "feture": String        // zigbee2mqtt feature name (power, state, temperature, etc.)
    }
}
```

in case if you manually remove the device or want a custom association please make sure that you've updated the configuration accordingly