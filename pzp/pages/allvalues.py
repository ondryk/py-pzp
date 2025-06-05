from pzp.client import PzpClient
from .page import PageParser
from .temps import TemperatureParser
from .states import RunningStateParser

class AllValuesParser(PageParser):
    """
    Parses page with running state of system components
    """
    def __init__(self, client:PzpClient):
        super().__init__(client, "/PAGE15.XML") # TODO dummy fetch, not parsed as others are parsed in following parsers
        self.temps_page = TemperatureParser(client)
        self.states_page = RunningStateParser(client)

    def parse(self):
        result = []
        
        temps = self.temps_page.parse()
        result.extend(temps)
        
        states = self.states_page.parse()
        result.extend(states)

        return result