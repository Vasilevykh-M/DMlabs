import requests
from lab1.utils.read_yaml import read_yaml


class OAuth():
    
    #приватные параметры для клчиков приложения и ссылки на сервак
    def __init__(self):
        cfg = read_yaml("conf.yaml")
        self._CLIENT_ID = cfg["client_id"]
        self._CLIENT_SECRET = cfg["client_secret"]
        self._REDIRECT_URI = cfg["redirect_uri"]

    def CLIENT_ID(self):
        return self._CLIENT_ID

    def CLIENT_SECRET(self):
        return self._CLIENT_SECRET

    def REDIRECT_URI(self):
        return self._REDIRECT_URI
    
    
    #создание ссылки для получения кода аутентификации
    def create_oath_link(self):
        params = {
            "client_id": self.CLIENT_ID(),
            "redirect_uri": self.REDIRECT_URI(),
            "scope": "repo, delete_repo",
            "response_type": "code",
        }
        endpoint = "https://github.com/login/oauth/authorize"
        response = requests.get(endpoint, params=params)
        url = response.url
        return url


    #обмен кода аутентификации на токен
    def exchange_code_for_access_token(self, code=None):
        params = {
            "client_id": self.CLIENT_ID(),
            "client_secret": self.CLIENT_SECRET(),
            "redirect_uri": self.REDIRECT_URI(),
            "code": code,
        }

        headers = {"Accept": "application/json"}
        endpoint = "https://github.com/login/oauth/access_token"
        response = requests.post(endpoint, params=params, headers=headers).json()
        print("exchange complete")
        return response["access_token"]

    def refresh_access_token(self, token):
        params = {
            "client_id": self.CLIENT_ID(),
            "client_secret": self.CLIENT_SECRET(),
            "refresh_token": token,
            "grant_type": "refresh_token",
        }

        headers = {"Accept": "application/json"}
        endpoint = "https://github.com/login/oauth/access_token"
        response = requests.post(endpoint, params=params, headers=headers).json()
        print("exchange complete")
        return response["access_token"]

