import re

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
url = "https://mail.psu.ru/"
driver.get(url)

# Ввод логина
email_input = driver.find_element(By.NAME, 'Username')
email_input.send_keys('')
email_input.send_keys(Keys.RETURN)

# Ожидание загрузки страницы ввода пароля
time.sleep(5)

# Ввод пароля
password_input = driver.find_element(By.NAME, 'Password')
password_input.send_keys('')
password_input.send_keys(Keys.RETURN)

# Ожидание загрузки главной страницы
time.sleep(10)

# Извлечение данных и сохранение в список словарей
emails_data = []
for i in range(2):
    emails = driver.find_elements(By.XPATH, "//tr[@class='borderbottom']")
    email = emails[i]
    td_with_second_link = email.find_element(By.XPATH, ".//td[position() = last()-2]//a")
    td_with_second_link.click()

    time.sleep(5)

    subject_text = driver.find_element(By.XPATH, "//h2[@class='msgSubject padRight']").text

    meta_data = driver.find_element(By.XPATH, "//div[@class='msgHeaders']").text

    sender = re.search(r"От Кого:\s*(.*)", meta_data).group(1)

    email_data = {
        "sender": sender,
        "subject": subject_text,
    }
    driver.back()
    emails_data.append(email_data)

# Закрытие браузера
driver.quit()

# Запись данных в JSON-файл
with open('emails.json', 'w', encoding='utf-8') as f:
    json.dump(emails_data, f, ensure_ascii=False, indent=4)

print("Данные успешно записаны в файл emails.json")