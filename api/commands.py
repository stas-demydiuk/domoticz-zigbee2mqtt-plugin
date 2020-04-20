from api.bridge import GetBridgeStatus, SetBridgePermitJoinStatus
from api.devices import GetDevices, GetDeviceState, SetDeviceState, RenameDevice, GetDeviceOTAUpdateStatus, UpdateDeviceFirmware
from api.groups import GetGroups, AddGroup, RemoveGroup, IncludeDevice, ExcludeDevice
from api.network_map import NetworkMap


commands = dict({
    'network_map': NetworkMap,
    'devices_get': GetDevices,
    'device_get_state': GetDeviceState,
    'device_get_ota_update_status': GetDeviceOTAUpdateStatus,
    'device_ota_update': UpdateDeviceFirmware,
    'device_rename': RenameDevice,
    'device_set': SetDeviceState,
    'bridge_getstatus': GetBridgeStatus,
    'bridge_set_permitjoin': SetBridgePermitJoinStatus,
    'groups_get': GetGroups,
    'group_add': AddGroup,
    'group_remove': RemoveGroup,
    'group_include': IncludeDevice,
    'group_exclude': ExcludeDevice,
})
