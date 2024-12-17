from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import json

# Настройка ChromeOptions
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Максимизировать окно браузера
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Путь к ChromeDriver

# Создание экземпляра WebDriver
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

# Открытие страницы Gmail
url = "https://mail.google.com/"
driver.get(url)

# Ввод логина
email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_input.send_keys('ваш_email@gmail.com')
email_input.send_keys(Keys.RETURN)

# Ожидание загрузки страницы ввода пароля
time.sleep(5)

# Ввод пароля
password_input = driver.find_element(By.XPATH, '//*[@name="password"]')
password_input.send_keys('ваш_пароль')
password_input.send_keys(Keys.RETURN)

# Ожидание загрузки главной страницы
time.sleep(10)

# Поиск элементов с письмами
email_elements = driver.find_elements(By.XPATH, '//*[@class="zA zE"]')

# Извлечение данных и сохранение в список словарей
emails_data = []
for email_element in email_elements:
    sender = email_element.find_element(By.XPATH, './/*[@class="zF"]').text
    subject = email_element.find_element(By.XPATH, './/*[@class="zE"]').text
    date = email_element.find_element(By.XPATH, './/*[@class="y2"]').text

    email_data = {
        "sender": sender,
        "subject": subject,
        "date": date
    }
    emails_data.append(email_data)

# Закрытие браузера
driver.quit()

# Запись данных в JSON-файл
with open('emails.json', 'w', encoding='utf-8') as f:
    json.dump(emails_data, f, ensure_ascii=False, indent=4)

print("Данные успешно записаны в файл emails.json")