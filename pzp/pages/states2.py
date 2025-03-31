from pzp.client import PzpClient
from .page import PageParser

class RunningStateParser2(PageParser):

    def __init__(self, client:PzpClient):
        super().__init__(client, "/PAGE74.XML")

    def parse(self):
        result = []
        #TODO add conditionally parsed values
        result.append(self.parse_val("B13: Pokojový terminál 1", "T4C6690D0"))

        return result