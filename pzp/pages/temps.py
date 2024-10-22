import re
from pzp.client import PzpClient
from datetime import datetime

#Temperature definitions
class TempDef:
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value

    def __str__(self) -> str:
        return f"{self.name}={self.value}"

class TemperatureParser:

    def __init__(self, client:PzpClient):
        self.client = client

    def retrieve(self, print_header: bool = True, sep: str = ";", debug: bool = False):
        temps_raw = self.client.get_page("/PAGE73.XML")
        if debug:
            print("Raw response")
            print(temps_raw)
        now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        tmps = self.parse(temps_raw)
   
        if print_header:
            print(f"Datum{sep}", end="")
            for i, item in enumerate(tmps):
                print(f"{sep if i > 0 else ''}{item.name}", end="")
        print()      
        print(f"{now}{sep}", end="")
        for i, item in enumerate(tmps):
            print(f"{sep if i > 0 else ''}{item.value}", end="")
        print()


    def parse(self, text: str):
        result = []
        try:
            result.append(TemperatureParser.parse_val(text, "B01: Teplota 1 sekundarní okruh", "T611D9BA9"))
            result.append(TemperatureParser.parse_val(text, "B02: Teplota 2 sekundarní okruh", "TAFAD1E97"))
            result.append(TemperatureParser.parse_val(text, "B03: Teplota v okolí výparníku", "TEA3D9DBA"))
            result.append(TemperatureParser.parse_val(text, "B04: Teplota na povrchu výparníku", "T328414A2"))
            result.append(TemperatureParser.parse_val(text, "B11: Teplota vratné vody z topení", "T715C92F2"))
            result.append(TemperatureParser.parse_val(text, "B12: Teplota TUV", "TBFEC17CC"))
            result.append(TemperatureParser.parse_val(text, "B07: Teplota na vstupu deskového výparníku", "TFC34919C"))
            result.append(TemperatureParser.parse_val(text, "B08: Teplota na výstupu deskového výparníku", "T089F00C8"))
        except Exception as e:
            print(f"Error during parsing: {e}")
            return []
        
        return result

    @staticmethod
    def parse_val(text: str, name: str, code: str) -> TempDef:
        pattern = fr'<INPUT NAME="__{code}_REAL_.1f"\sVALUE="(.*?)"'
        r = re.compile(pattern)

        match = r.search(text)
        if match:
            value = float(match.group(1))
            return TempDef(name, value)
        else:
            raise ValueError(f"Could not find value for code: {code}")