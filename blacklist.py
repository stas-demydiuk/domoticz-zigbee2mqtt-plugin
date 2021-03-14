import domoticz
import re

def has(device_id):
    blacklist_raw = domoticz.get_plugin_config('blackList')

    if blacklist_raw == '':
        return False

    blacklist = blacklist_raw.split(';')

    for pattern in blacklist:
        if re.match(pattern.strip(), device_id):
            return True
    
    return False

