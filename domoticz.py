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

def get_plugin_config(key = None):
    config = {
        "trackLinkQuality": False if plugin.Parameters["Mode4"] == 'No' else True,
        "useBatteryDevices": False if plugin.Parameters["Mode5"] == 'No' else True
    }

    return config[key] if key in config else config