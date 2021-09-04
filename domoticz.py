import DomoticzEx as Domoticz
import plugin

def log(message):
    return Domoticz.Log(message)

def error(message):
    return Domoticz.Error(message)

def debug(message):
    return Domoticz.Debug(message)

def get_devices():
    return plugin.Devices

def get_device(device_id, unit):
    devices = get_devices()

    try:
        return devices[device_id].Units[unit]
    except Exception as e:
        return None

def create_device(**kwargs):
    device = Domoticz.Unit(**kwargs)
    device.Create()
    return device

def get_configuration():
    return Domoticz.Configuration()

def set_configuration(value):
    return Domoticz.Configuration(value)

def get_first_available_unit():
    devices = get_devices()

    for i in range(1, 254):
        if i not in devices:
            return i

def get_plugin_parameters():
    return plugin.Parameters

def get_plugin_config(key = None):
    parameters = get_plugin_parameters()
    config = {
        "trackLinkQuality": False if parameters["Mode4"] == 'No' else True,
        "useBatteryDevices": False if parameters["Mode5"] == 'No' else True,
        "blackList": parameters["Mode2"]
    }

    return config[key] if key in config else config
