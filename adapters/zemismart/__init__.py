from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.zemismart.ZMCSW002D import ZMCSW002D
from adapters.zemismart.ZML03EZ import ZML03EZ

zemismart_adapters = {
    'ZM-CSW002-D': ZMCSW002D,   # Zemismart ZM-CSW002-D 2 gang switch
    'ZM-L03E-Z': ZML03EZ,       # Zemismart ZM-L03E-Z 3 gang with neutral wire switch
}
