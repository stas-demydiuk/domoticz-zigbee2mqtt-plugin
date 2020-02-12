from adapters.rgbw_adapter import RGBWAdapter
from adapters.generic.blind_adapter import BlindAdapter
from adapters.zemismart.ZMCSW002D import ZMCSW002D
from adapters.zemismart.ZML03EZ import ZML03EZ

zemismart_adapters = {
    'LXZB-12A': RGBWAdapter,    # Zemismart RGB LED downlight
    'ZM-CSW002-D': ZMCSW002D,   # Zemismart ZM-CSW002-D 2 gang switch
    'ZM-CSW032-D': BlindAdapter,# Zemismart Curtain/roller blind switch
    'ZM-L03E-Z': ZML03EZ,       # Zemismart ZM-L03E-Z 3 gang with neutral wire switch
}
