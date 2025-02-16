from app.db import db

# Создание индексов
db.products.create_index("name", unique=True)
db.users.create_index("email", unique=True)

print("Database initialized successfully!")
