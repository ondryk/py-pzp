import requests
from datetime import datetime
from .pages.temps import TemperatureParser
import urllib3


class PzpClient:
    def __init__(self, server_base: str, user: str, password: str):
        self.server_base = server_base
        self.user = user
        self.passwd = password
        self.client = requests.Session()
        self.client.verify = False
        self.client.cookies = requests.cookies.RequestsCookieJar()
        urllib3.disable_warnings() # disable tls/https warns

    @classmethod
    def create_and_login(cls, server_base: str, user: str, password: str):
        cli = cls(server_base, user, password)
        cli.login()
        return cli

    def get_url(self, endpoint: str) -> str:
        return f"{self.server_base}{endpoint}"

    def login(self):
        # Send GET request for login cookie
        resp = self.client.get(self.get_url("/SYSWWW/LOGIN.XML"))
        resp.raise_for_status()

        # Send POST request with login credentials
        login_body = f"USER={self.user}&PASS={self.passwd}"
        resp_login = self.client.post(self.get_url("/SYSWWW/LOGIN.XML"), data=login_body)
        resp_login.raise_for_status()

    def print_temps(self, print_header: bool, sep: str):
        temps_resp = self.client.get(self.get_url("/PAGE73.XML"))
        temps_resp.raise_for_status()
        text = temps_resp.text
        #print(text)
        now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        # Mock TemperatureParser class (you need to replace this with actual parser logic)
        tmps = TemperatureParser.parse(text)
        #prepsat ze se parser vytvori, vezme si klienta, zavola se get, a to vyblije pole hodnot
       # print(tmps)
        if print_header:
            print(f"Datum{sep}", end="")
            for i, item in enumerate(tmps):
                print(f"{sep if i > 0 else ''}{item.name}", end="")
        print()      
        print(f"{now}{sep}", end="")
        for i, item in enumerate(tmps):
            print(f"{sep if i > 0 else ''}{item.value}", end="")
        print()


    def logout(self):
        #try:
            resp = self.client.get(self.get_url("/LOGOUT.XML"))
            resp.raise_for_status()
       # except RequestException as e:
        #    raise ApplicationErrors(f"Unable to logout: {str(e)}")


