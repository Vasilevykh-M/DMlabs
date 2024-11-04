import json
import requests

from lab1.git_.oauth_api import OAuth
from lab1.git_.server import Server


class ApiGit():

    def __init__(self):

        oauth = OAuth()
        link = oauth.create_oath_link()
        serv = Server()
        print(f"Перейдите по ссылке, чтобы запустить аутентификацию с помощью GitHub: {link}")
        serv.start()
        code = serv.get_code()

        if code == '':
            exit(0)

        access_token = oauth.exchange_code_for_access_token(code)

        self.__access_token = access_token
        self.__login = self.__get_name()

    def get_login(self):
        return self.__login


    # получении имени авторизированного пользователя
    def __get_name(self):
        headers = {"Authorization": f"token {self.__access_token}"}
        endpoint = "https://api.github.com/user"
        user = requests.get(endpoint, headers=headers).json()
        return (user['login'])


    # вывести список всех репозиториев у пользователя
    def print_user_repo(self):
        headers = {"Authorization": f"token {self.__access_token}"}
        endpoint = "https://api.github.com/user/repos"
        params = {
            "state": "open",
        }
        repos = requests.get(endpoint, headers=headers, params=params).json()
        for repo in repos:
            print('repo name: ', repo['name'])