# Используем официальный Python образ
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей (если есть)
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы
COPY . /app/

# Указываем команду для запуска приложения
CMD ["python", "mongo_.py"]