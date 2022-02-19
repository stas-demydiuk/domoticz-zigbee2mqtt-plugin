# Adapter for cc2530 zigbee firmware found on http://ptvo.info/zigbee-switch-configurable-firmware-router-199/

from adapters.base_adapter import Adapter
from adapters.on_off_switch_adapter import OnOffSwitchAdapter
from devices.text_sensor import TextSensor
from devices.switch.on_off_switch import OnOffSwitch

#PTVOID = {'input1' : 'bottom_left',
#		  'input2' : 'bottom_right',
#		  'input3' : 'top_left',
#		  'input4' : 'top_right',
#         'input5' : 'center'}

#update to latest zigbee2MQTT 1.14.3 compatible
PTVOID = {'input1' : 'l1', 'input2' : 'l2', 'input3' : 'l3', 'input4' : 'l4', 'input5' : 'l5', 'input6' : 'l6', 'input7' : 'l7', 'input8' : 'l8'}

class PtvoSwitch(Adapter):
    def __init__(self):
        super().__init__()
        self.devices.append(TextSensor('click', 'click', ' (input)'))
        self.switch={}
        for ptvo in PTVOID:
            self.switch[ptvo] = OnOffSwitch(ptvo, 'state_' + PTVOID[ptvo], ' (' + ptvo + ')')
            self.devices.append(self.switch[ptvo])

    def handle_command(self, alias, device, command, level, color):
        device_data = self._get_legacy_device_data()
        self.switch[alias].handle_command(device_data, command, level, color)
        
        return {
            'topic': '/'.join([device_data['friendly_name'], PTVOID[alias], 'set']),
            'payload': command.upper()
        }
