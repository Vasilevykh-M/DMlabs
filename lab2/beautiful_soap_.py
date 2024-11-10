import requests
from bs4 import BeautifulSoup

# URL страницы
url = "https://www.firefly.store/search?q=Rockchip&options%5Bprefix%5D=last"

# Отправляем запрос
response = requests.get(url)
response.raise_for_status()  # Проверим на ошибки

# Парсим HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Находим все товары
products = soup.find_all('div', class_='card__information')

# Извлекаем данные
for product in products:
    name = product.find('a', class_='full-unstyled-link')
    price = product.find('span', class_='price-item price-item--regular')

    if name and price:
        print(f"Название: {name.get_text(strip=True)}")
        print(f"Цена: {price.get_text(strip=True)}")
        print("-" * 30)