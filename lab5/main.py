from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json

# Настройка ChromeOptions
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в режиме без графического интерфейса
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Путь к ChromeDriver

# Создание экземпляра WebDriver
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)
# Открытие страницы
url = "https://quotes.toscrape.com/js/"
driver.get(url)

# Ожидание загрузки страницы
time.sleep(5)  # Можно использовать WebDriverWait для более точного ожидания

# Поиск элементов с цитатами
quote_elements = driver.find_elements(By.CLASS_NAME, "quote")

# Извлечение данных и сохранение в список словарей
quotes_data = []
for quote_element in quote_elements:
    text = quote_element.find_element(By.CLASS_NAME, "text").text
    author = quote_element.find_element(By.CLASS_NAME, "author").text
    tags = [tag.text for tag in quote_element.find_elements(By.CLASS_NAME, "tag")]

    quote_data = {
        "text": text,
        "author": author,
        "tags": tags
    }
    quotes_data.append(quote_data)

# Закрытие браузера
driver.quit()

# Запись данных в JSON-файл
with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(quotes_data, f, ensure_ascii=False, indent=4)

print("Данные успешно записаны в файл quotes.json")