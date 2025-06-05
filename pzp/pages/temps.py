from pzp.client import PzpClient
from .page import PageParser
from .states2 import RunningStateParser2

class TemperatureParser(PageParser):

    def __init__(self, client:PzpClient):
        super().__init__(client, "/PAGE73.XML")
        self.running_states2 = RunningStateParser2(client)


    def parse(self):
        result = []
        result.append(self.parse_val("B01: Teplota 1 sekundarní okruh", "T611D9BA9"))
        result.append(self.parse_val("B02: Teplota 2 sekundarní okruh", "TAFAD1E97"))
        result.append(self.parse_val("B03: Teplota v okolí výparníku", "TEA3D9DBA"))
        result.append(self.parse_val("B04: Teplota na povrchu výparníku", "T328414A2"))
        result.append(self.parse_val("B11: Teplota vratné vody z topení", "T715C92F2"))
        result.append(self.parse_val("B12: Teplota TUV", "TBFEC17CC"))
        result.append(self.parse_val("B07: Teplota na vstupu deskového výparníku", "TFC34919C"))
        result.append(self.parse_val("B08: Teplota na výstupu deskového výparníku", "T089F00C8"))

        # Append states from secondary page to output
        running_states2 = self.running_states2.parse()
        result.extend(running_states2)

        return result