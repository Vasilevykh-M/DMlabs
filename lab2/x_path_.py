import requests
from lxml import html

from lab2.utils.to_json import to_json

# URL страницы
url = "https://www.firefly.store/search?q=Rockchip&options%5Bprefix%5D=last"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'Connection': 'keep-alive',
}

response = requests.get(url, headers=headers)
response.raise_for_status()  # Проверим на ошибки

# Парсим HTML
tree = html.fromstring(response.content)

# Извлекаем данные с помощью XPath
product_names = tree.xpath('//a[@class="full-unstyled-link"]')
prices = tree.xpath('//span[@class="price-item price-item--regular"]/text()')

result = []

# Выводим результаты
for name, price in zip(product_names, prices):
    print(f"Название: {name.text.strip()}")
    print(f"Цена: {price.strip()}")
    print("-" * 30)

    result.append({"name": name.text.strip(), "price": price.strip()})

to_json(result)