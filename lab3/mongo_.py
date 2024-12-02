import pymongo
from pymongo import MongoClient
import json

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['mydatabase']  # Создаем/подключаем базу данных
collection = db['products']  # Коллекция товаров

# Функция для загрузки данных из файла в базу
def load_data_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            collection.insert_one(item)
        print(f"Загружено {len(data)} записей в базу данных.")

# Функция для выборки товаров с ценой больше 100
def get_products_with_price_above_100():
    query = {"Цена": {"$gt": 100}}  # Выборка товаров с ценой больше 100
    products = collection.find(query)
    for product in products:
        print(f"Название: {product['Название']}, Цена: {product['Цена']}")

# Функция для добавления нового товара
def add_product(name, price):
    product = {"Название": name, "Цена": price}
    collection.insert_one(product)
    print(f"Товар '{name}' с ценой {price} добавлен в базу.")

if __name__ == "__main__":
    # Пример использования
    load_data_from_file('result.json')  # Загружаем данные из файла
    get_products_with_price_above_100()  # Выводим товары с ценой выше 100
    add_product("Новый товар", 150.75)  # Добавляем новый товар