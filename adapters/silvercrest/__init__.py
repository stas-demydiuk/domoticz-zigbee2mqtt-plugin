from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from adapters.contact_adapter import ContactAdapter
from devices.sensor.door_contact import DoorContactSensor
from adapters.generic.motion_sensor import MotionSensorAdapter
from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.rgbw_adapter import RGBWAdapter
from adapters.silvercrest.HG06336 import HG06336



silvercrest_adapters = {
    'TY0202': MotionSensorAdapter,      # Silvercrest Smart Window or Door sensor
    'TY0203': ContactAdapter,           # Silvercrest Smart Window or Door sensor
    'HG06336':HG06336,                  # Silvercrest Smart Window or Door sensor
    'TY0111': OnOffSwitchAdapter,       # Silvercrest Smart Home Socket
}
