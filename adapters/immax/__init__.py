from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.immax.immax_07046L import Immax07046L

immax_adapters = {
    'IM-Z3.0-DIM': DimmableBulbAdapter,     # Immax LED E14/230V C35 5W TB 440LM ZIGBEE DIM
    '07046L': Immax07046L,                  # Immax 4-Touch single click buttons
}