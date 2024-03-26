from adapters.base_adapter import Adapter
from adapters.onesti.easyCodeTouch_v1_lock import EasyCodeTouch_v1
from adapters.onesti.nimly_lock import NimlyLock


onesti_adapters = {
    'easyCodeTouch_v1': EasyCodeTouch_v1,  # EasyCodeTouch V1
    'Nimly': NimlyLock,  # Nimly (Pro, Touch, Code, In)
}
