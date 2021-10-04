---
name: New device feature support
about: Ask to add support for a new device feature
title: '`feature_name` feature support'
labels: new feature
assignees: ''

---

**Feature description**
Put general information about feature here i.e. 

Example:
On/off state of the switch

**Feature definition**
Feature definition could be retrieved in a several ways:
 - from mqtt message when you publish message with topic `zigbee2mqtt/bridge/config/devices`
 - from Domoticz log when you run plugin in Debug mode
 
Example:
```
{
    "access":7,
    "description":"On/off state of the switch",
    "name":"state",
    "property":"state",
    "type":"binary",
    "value_off":"OFF",
    "value_on":"ON",
    "value_toggle":"TOGGLE"
}
```

**Related Devices**
Insert the device page link on zigbee2mqtt.io that supports (exposes) that feature 

Example:
https://www.zigbee2mqtt.io/devices/TS0121_plug.html