from pzp.client import PzpClient
from .page import PageParser

class OverallInfoPage(PageParser):
    """
    Process first page after login with overall info
    """
    def __init__(self, client:PzpClient):
        super().__init__(client, "/PAGE13.XML")

    def parse(self):
        result = []
        result.append(self.parse_bool("S09: Blokování signálem HDO", "T48897449"))
        result.append(self.parse_bool("S10: Porucha", "T32F2292C"))
        return result   