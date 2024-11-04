import requests
import server
class OAuth():
    
    #приватные параметры для клчиков приложения и ссылки на сервак
    def __init__(self):
        self._CLIENT_ID = "fb21d87396f88ed06a60"
        self._CLIENT_SECRET = "38718f76d743f5d89fd148551b2bbdc5af6da990"
        self._REDIRECT_URI = 'http://localhost:8000/'

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

