from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.rgbw_adapter import RGBWAdapter
from adapters.innr.SP120 import InnrSP120Plug


innr_adapters = {
    'BY 165': DimmableBulbAdapter,      # Innr B22 Bulb dimmable
    'BY 185 C': RGBWAdapter,            # Innr B22 Bulb RGBW
    'BY 285 C': RGBWAdapter,            # Innr B22 Bulb RGBW
    'DL 110 N': DimmableBulbAdapter,    # Innr Spot narrow
    'DL 110 W': DimmableBulbAdapter,    # Innr Spot wide
    'FL 130 C': RGBWAdapter,            # Innr Color Flex LED strip
    'PL 110': DimmableBulbAdapter,      # Innr Puck Light
    'RB 145': DimmableBulbAdapter,      # Innr E14 Candle
    'RB 165': DimmableBulbAdapter,      # Innr E27 Bulb
    'RB 175 W': DimmableBulbAdapter,    # Innr E27 Bulb warm dimming
    'RB 178 T': DimmableCtBulbAdapter,  # Innr Smart bulb tunable white E27
    'RB 185 C': RGBWAdapter,            # Innr E27 Bulb RGBW
    'RB 245': DimmableBulbAdapter,      # Innr E14 Candle
    'RB 248 T': DimmableCtBulbAdapter,  # Innr E14 Candle with white spectrum
    'RB 250 C': RGBWAdapter,            # Innr E14 Bulb RGBW
    'RB 265': DimmableBulbAdapter,      # Innr E27 Bulb
    'RB 278 T': DimmableBulbAdapter,    # Innr E27 Bulb
    'RB 285 C': RGBWAdapter,            # Innr E27 Bulb RGBW
    'RF 263': DimmableBulbAdapter,      # Innr E27 filament bulb dimmable
    'RF 265': DimmableBulbAdapter,      # Innr E27 bulb filament clea
    'RS 122': DimmableBulbAdapter,      # Innr GU10 Spot
    'RS 125': DimmableBulbAdapter,      # Innr GU10 Spot
    'RS 128 T': DimmableCtBulbAdapter,  # Innr GU10 Spot 350 lm, dimmable, white spectrum
    'RS 225': DimmableBulbAdapter,      # Innr GU10 Spot
    'RS 228 T': DimmableCtBulbAdapter,  # Innr GU10 Spot 350 lm
    'SL 110 M': DimmableBulbAdapter,    # Innr Spot Flex medium
    'SL 110 N': DimmableBulbAdapter,    # Innr Spot Flex narrow
    'SL 110 W': DimmableBulbAdapter,    # Innr Spot Flex wide
    'SP 120': InnrSP120Plug,            # Innr Smart plug
    'SP 222': OnOffSwitchAdapter,       # Innr Smart plug
    'ST 110': DimmableBulbAdapter,      # Innr Strip Light
    'UC 110': DimmableBulbAdapter,      # Innr Under Cabinet Light
}