from adapters.generic.plug import PlugAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.rgbw_adapter import RGBWAdapter


innr_adapters = {
    'AE 280 C': RGBWAdapter,            # Innr E26 bulb RGBW
    'BY 185 C': RGBWAdapter,            # Innr B22 Bulb RGBW
    'BY 285 C': RGBWAdapter,            # Innr B22 Bulb RGBW
    'FL 130 C': RGBWAdapter,            # Innr Color Flex LED strip
    'OFL 120 C': RGBWAdapter,           # Innr Outdoor flex light colour LED strip 2m, 550lm, RGBW
    'OFL 140 C': RGBWAdapter,           # Innr Outdoor flex light colour LED strip 4m, 1000lm, RGBW
    'OSL 130 C': RGBWAdapter,           # Innr Outdoor smart spot colour, 230lm/spot, RGBW
    'RB 148 T': DimmableCtBulbAdapter,  # Innr E14 candle with white spectrum
    'RB 178 T': DimmableCtBulbAdapter,  # Innr Smart bulb tunable white E27
    'RB 185 C': RGBWAdapter,            # Innr E27 Bulb RGBW
    'RB 248 T': DimmableCtBulbAdapter,  # Innr E14 Candle with white spectrum
    'RB 250 C': RGBWAdapter,            # Innr E14 Bulb RGBW
    'RB 278 T': RGBWAdapter,    # Innr E27 Bulb tunable white
    'RB 285 C': RGBWAdapter,            # Innr E27 Bulb RGBW
    'RS 128 T': DimmableCtBulbAdapter,  # Innr GU10 Spot 350 lm, dimmable, white spectrum
    'RS 228 T': DimmableCtBulbAdapter,  # Innr GU10 Spot 350 lm
    'RS 229 T': DimmableCtBulbAdapter,  # Innr GU10 Spot 350 lm, dimmable, white spectrum
    'RS 230 C': RGBWAdapter,            # Innr GU10 spot 350 lm, dimmable, RGBW
    'SP 120': PlugAdapter,              # Innr Smart plug
}