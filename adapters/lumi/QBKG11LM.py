import Domoticz
import json
from adapters.lumi.QBKG04LM import QBKG04LM
from devices.sensor.kwh import KwhSensor


class QBKG11LM(QBKG04LM):
    def __init__(self, devices):
        super().__init__(devices)

        self.devices.append(KwhSensor(devices, 'kwh', ['power']))
