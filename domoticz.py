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