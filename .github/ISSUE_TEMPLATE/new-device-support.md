---
name: New device support
about: Ask to add support for new device
title: ''
labels: new device
assignees: ''

---

**Device description**
Put general device information here

**Zigbee2mqtt page**
Insert the device page link on zigbee2mqtt.io i.e. https://www.zigbee2mqtt.io/devices/MCLH-08.html

**MQTT message with device information**
PUT here the device data you receive when publish message with topic
`zigbee2mqtt/bridge/config/devices`, as example
```
{"ieeeAddr":"0x00158d0001bd0e35","type":"EndDevice","model":"WXKG01LM","friendly_name":"0x00158d0001bd0e35"}
```

**MQTT messages from device**
Put here examples of MQTT messages with different states you've received from device, as example
```
zigbee2mqtt:info 2018-10-28 13:34:09 MQTT publish, topic: 'zigbee2mqtt/WeatherGuestRoom', payload: '{"temperature":24.59,"linkquality":39,"humidity":36.56,"pressure":990,"battery":"37.00","voltage":2975}'

zigbee2mqtt:info 2018-10-28 13:34:09 MQTT publish, topic: 'zigbee2mqtt/WeatherGuestRoom', payload: '{"temperature":24.59,"linkquality":39,"humidity":37.55,"pressure":990,"battery":"37.00","voltage":2975}'

zigbee2mqtt:info 2018-10-28 13:34:09 MQTT publish, topic: 'zigbee2mqtt/WeatherGuestRoom', payload: '{"temperature":24.59,"linkquality":39,"humidity":37.55,"pressure":989,"battery":"37.00","voltage":2975}'
```

**MQTT state change commands**
If device supports state change put MQTT topics + payload examples to change device state here
