from api.network_map import NetworkMap
from api.get_devices import GetDevices
from api.device_rename import RenameDevice
from api.device_set import SetDeviceState
from api.bridge_status import GetBridgeStatus, SetBridgePermitJoinStatus
from api.groups import GetGroups, AddGroup, RemoveGroup, IncludeDevice, ExcludeDevice


commands = dict({
    'network_map': NetworkMap,
    'devices_get': GetDevices,
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
