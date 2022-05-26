import domoticz

def get_config_item(key=None, default={}):
    value = default

    try:
        config = domoticz.get_configuration()

        if (key != None):
            value = config[key] # only return requested key if there was one
        else:
            value = config      # return the whole configuration if no key
    except KeyError:
        value = default
    except Exception as inst:
        domoticz.error("Domoticz.Configuration read failed: '"+str(inst)+"'")
    
    return value
    
def set_config_item(key, value):
    config = {}

    try:
        config = domoticz.get_configuration()
        if (key != None):
            config[key] = value
        else:
            config = value  # set whole configuration if no key specified

        config = domoticz.set_configuration(config)
    except Exception as inst:
        domoticz.error("Domoticz.Configuration operation failed: '"+str(inst)+"'")

    return config

def get_alias_by_zigbee(device_address, feature_name, endpoint):
    aliases = get_config_item('aliases', [])

    for item in aliases:
        zigbee_data = item['zigbee']

        if zigbee_data['address'] == device_address and zigbee_data['feature'] == feature_name and zigbee_data['endpoint'] == endpoint:
            return item

    return None

def get_zigbee_feature_device(device_address, feature_name, endpoint):
    item = get_alias_by_zigbee(device_address, feature_name, endpoint)

    if item != None:
        domoticz_data = item['domoticz']
        return domoticz.get_device(domoticz_data['device_id'], domoticz_data['unit'])

    return None

def get_zigbee_feature_data(device_id, unit):
    aliases = get_config_item('aliases', [])

    for item in aliases:
        domoticz_data = item['domoticz']

        if domoticz_data['device_id'] == device_id and domoticz_data['unit'] == unit:
            return item

def set_zigbee_feature_device(device_address, feature_name, endpoint, device_id, unit, alias):
    aliases = get_config_item('aliases', [])

    if get_zigbee_feature_data(device_id, unit):
        return None

    aliases.append({
        'zigbee': {
            'address': device_address,
            'feature': feature_name,
            'endpoint': endpoint
        },
        'domoticz': {
            'device_id': device_id,
            'unit': unit,
            'legacy_alias': alias
        }
    })

    return set_config_item('aliases', aliases)

def get_device_available_unit(device_address):
    aliases = get_config_item('aliases', [])

    for i in range(1, 254):
        exists = False
        
        for item in aliases:
            if item['zigbee']['address'] == device_address and item['domoticz']['unit'] == i:
                exists = True
                break
        
        if not exists:
            return i

def remove_device(device_id, unit):
    aliases = get_config_item('aliases', [])
    item = get_zigbee_feature_data(device_id, unit)

    if (item == None):
        return

    aliases.remove(item)
    return set_config_item('aliases', aliases)