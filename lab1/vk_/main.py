import requests

from lab1.utils.to_json import vk_json_private

# Вставьте ваш токен доступа
ACCESSTOKEN = ''
USERID = 'me'  # Для текущего пользователя используем 'me'
APIVERSION = '5.199'  # Версия API

def getusergroups(userid):
    url = 'https://api.vk.com/method/groups.get'
    params = {
        'userid': userid,
        'extended': 1,  # Получаем дополнительную информацию о группах
        'access_token': ACCESSTOKEN,
        'v': APIVERSION
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'response' in data:
        groups = data['response']['items']
        return groups
    else:
        print("Error:", data)
        return []

def main():
    groups = getusergroups(USERID)
    if groups:
        vk_json_private(groups)
    else:
        print("Группы не найдены или ошибка при получении данных.")
main()