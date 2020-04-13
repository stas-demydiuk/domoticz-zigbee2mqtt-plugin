from api.network_map import NetworkMap
from api.get_devices import GetDevices
from api.device_rename import RenameDevice
from api.device_set import SetDeviceState


commands = dict({
    'network_map': NetworkMap,
    'devices_get': GetDevices,
    'device_rename': RenameDevice,
    'device_set': SetDeviceState,
})
