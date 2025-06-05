from pzp.client import PzpClient
from .page import PageParser
from .overall import OverallInfoPage

class RunningStateParser(PageParser):
    """
    Parses page with running state of system components
    """
    def __init__(self, client:PzpClient):
        super().__init__(client, "/PAGE15.XML")
        self.overall_page = OverallInfoPage(client)

    def parse(self):
        result = []
        result.append(self.parse_bool("S01: Běh kompresoru", "T7E3FC003"))
        result.append(self.parse_bool("S02: Oběhové čerpadlo topení č.4", "T1F74EFF9"))
        result.append(self.parse_bool("S03: Ohřev TUV", "TB468BAE2"))
        result.append(self.parse_bool("S04: Přímotopný ohřev TUV", "TB7060E15"))
        result.append(self.parse_bool("S05: Provoz primárního okruhu", "T43337318"))
        result.append(self.parse_bool("S06: Oběhové čerpadlo sekundárního okruhu", "T782CD2B5"))
        result.append(self.parse_bool("S07: Běh elektrokotle č.1", "T8E22B3AD"))
        result.append(self.parse_bool("S08: Běh elektrokotle č.2", "T95CF3693"))

        # Append states from overall page to output
        overall = self.overall_page.parse()
        result.extend(overall)

        return result