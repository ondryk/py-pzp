from pzp.client import PzpClient
from .page import PageParser

class RunningStateParser(PageParser):

    def __init__(self, client:PzpClient):
        super().__init__(client, "/PAGE15.XML")

    def parse(self, text: str):
        result = []
        try:
            result.append(self.parse_bool("Běh kompresoru", "T7E3FC003"))
            result.append(self.parse_bool("Oběhové čerpadlo topení 1", "T1F74EFF9"))
            result.append(self.parse_bool("Ohřev TUV", "TB468BAE2"))
            result.append(self.parse_bool("Přímotopný ohřev TUV", "TB7060E15"))
            result.append(self.parse_bool("Provoz primárního okruhu", "T43337318"))
            result.append(self.parse_bool("Oběhové čerpadlo sekundárního okruhu", "T782CD2B5"))
            result.append(self.parse_bool("Běh elektrokotle č.1", "T8E22B3AD"))
            result.append(self.parse_bool("Běh elektrokotle č.2", "T95CF3693"))
        except Exception as e:
            print(f"Error during parsing: {e}")
            return []
        
        return result   