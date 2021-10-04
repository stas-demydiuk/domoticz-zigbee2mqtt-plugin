import domoticz

bridge_info = {}
zigbee_devices = []
zigbee_groups = []

def handle_mqtt_message(topic, message):
    if topic == 'bridge/devices':
        domoticz.log('Received available devices list from bridge')
        global zigbee_devices 
        zigbee_devices = message
        return

    if topic == 'bridge/groups':
        domoticz.log('Received available devices groups from bridge')
        global zigbee_groups
        zigbee_groups = message
        return

    if topic == 'bridge/info':
        global bridge_info
        bridge_info = message
        return