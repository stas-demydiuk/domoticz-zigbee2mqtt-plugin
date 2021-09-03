import Domoticz
import plugin

def log(message):
    return Domoticz.Log(message)

def error(message):
    return Domoticz.Error(message)

def debug(message):
    return Domoticz.Debug(message)

def get_devices():
    return plugin.Devices

def create_device(**kwargs):
    return Domoticz.Device(**kwargs).Create()

def get_first_available_unit():
    devices = get_devices()

    for i in range(1, 254):
        if i not in devices:
            return i

def get_plugin_config(key = None):
    config = {
        "trackLinkQuality": False if plugin.Parameters["Mode4"] == 'No' else True,
        "useBatteryDevices": False if plugin.Parameters["Mode5"] == 'No' else True,
        "blackList": plugin.Parameters["Mode2"]
    }

    return config[key] if key in config else config