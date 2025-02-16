# Развертывание FastAPI с MongoDB

## Перейдите в корневуб папку проекта

## Установка зависимостей

pip install -r requirements.txt


## Запуск MongoDB (локально)

Запустите MongoDB

mongod --dbpath "C:\data\db"

## Запуск приложения

uvicorn main:app --host 0.0.0.0 --port 8000 --reload


## Доступ к API
Перейдите по адресу `http://localhost:8000/docs` для просмотра Swagger UI.