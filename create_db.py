import sqlite3

# Подключение к базе данных (если файла нет, он будет создан)
conn = sqlite3.connect('contact_form.db')
cursor = conn.cursor()

# Создание таблицы для хранения данных
cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL
)''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
