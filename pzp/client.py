import requests
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

    def get_page(self, page:str):
        get_resp = self.client.get(self.get_url(page))
        get_resp.raise_for_status()
        return get_resp.text
      
      

    def logout(self):
        resp = self.client.get(self.get_url("/LOGOUT.XML"))
        resp.raise_for_status()


