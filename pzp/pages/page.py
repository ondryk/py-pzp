import re
from pzp.client import PzpClient
from datetime import datetime
from pzp.values import FloatValue,BoolValue
from abc import ABC, abstractmethod

class PageParser(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """

    def __init__(self, client:PzpClient, page_path:str):
        self.client = client
        self.page_path = page_path
        self.raw_page_text = None

    def fetch_data(self):
        self.raw_page_text = self.client.get_page(self.page_path)

    def print(self, print_header: bool = True, sep: str = ";", debug: bool = False):
        self.fetch_data()

        if debug:
            print("Raw response")
            print(self.raw_page_text)

        tmps = self.parse()

        now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        if print_header:
            print(f"Datum{sep}", end="")
            for i, item in enumerate(tmps):
                print(f"{sep if i > 0 else ''}{item.name}", end="")
            print()

        print(f"{now}{sep}", end="")
        for i, item in enumerate(tmps):
            print(f"{sep if i > 0 else ''}{item.value}", end="")
        print()

    @abstractmethod
    def parse(self):
        """
        Actual parsing logic from page that assumes fetch has been already performed
        """

    def parse_val(self, name: str, code: str) -> FloatValue:
        r = re.compile(fr'<INPUT NAME="__{code}_REAL_.1f"\sVALUE="(.*?)"')

        match = r.search(self.raw_page_text)
        if match:
            value = float(match.group(1))
            return FloatValue(name, value)
        else:
            raise ValueError(f"Could not find value for code: {code}")

    def parse_bool(self, name: str, code: str) -> BoolValue:
        pattern = fr'<INPUT NAME="__{code}_BOOL_i"\sVALUE="(.*?)"'
        r = re.compile(pattern)

        match = r.search(self.raw_page_text)
        if match:
            num = int(match.group(1))
    #      value = bool(num)
            return BoolValue(name, num)
        else:
            raise ValueError(f"Could not find value for code: {code}")