from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch
import Domoticz

class TradfriRemoteCloseOpen(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'click')
        #self.switch.add_level('On', 'open')
        #self.switch.add_level('Off', 'close')
        #self.switch.add_level('None', '')
        self.switch.add_level('Up', 'open')
        self.switch.add_level('Down', 'close')
        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_BUTTONS)


        self.devices.append(self.switch)


    def handleCommand(self, alias, device, device_data, command, level, color):
        Domoticz.Debug(str(command)+str(level)+str(color))
        self.switch.handle_command(device_data, command, level, color)
        
        return {
            'topic': device_data['friendly_name'] + '/set',
            'payload': json.dumps({
                "state": command.upper()
            })
        }

