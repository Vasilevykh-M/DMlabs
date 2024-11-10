import requests

# Замените эти значения своими данными
client_id = "52615694"
scope = "groups"  # Права доступа, которые запрашиваются (например, groups)


def get_authorization_url():
    url = f"https://oauth.vk.com/authorize?client_id={client_id}&display=page&scope={scope}&response_type=token&v=5.131"
    return url


def exchange_code_for_token(code):
    data = {
        "client_id": client_id,
        "code": code
    }

    response = requests.post("https://oauth.vk.com/access_token", data=data)
    if response.status_code == 200:
        json_response = response.json()
        access_token = json_response["access_token"]
        user_id = json_response["user_id"]
        print(f"Пользовательский токен: {access_token}")
        print(f"ID пользователя: {user_id}")
        return access_token
    else:
        raise Exception(response.text)


if __name__ == "__main__":
    auth_url = get_authorization_url()
    print(f"Перейдите по этой ссылке для авторизации: {auth_url}")

    # Здесь вы должны получить код после авторизации и передать его в функцию обмена кода на токен
    code = input("Введите полученный код: ")
    token = exchange_code_for_token(code)