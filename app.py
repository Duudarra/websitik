from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
import requests 
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://duudarra.github.io"}})

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('contact_form.db')
    conn.row_factory = sqlite3.Row  # Это позволит обращаться к столбцам по имени
    return conn

def send_telegram_message(message):
    token = os.getenv('TELEGRAM_BOT_TOKEN')  # Получаем токен из переменной окружения
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    # Формирование URL для отправки сообщения
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': message
    }
    
    # Отправка POST запроса в Telegram
    response = requests.post(url, data=params)
    
    if response.status_code != 200:
        print("Ошибка при отправке сообщения в Telegram")
    else:
        print("Сообщение успешно отправлено в Telegram")

# Эндпоинт для получения всех записей
@app.route('/responces', methods=['GET'])
def get_responses():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages")
    rows = cursor.fetchall()
    conn.close()

    responses = [{'id': row['id'], 'name': row['name'], 'email': row['email'], 'message': row['message']} for row in rows]
    return jsonify(responses)

# Эндпоинт для добавления новой записи
@app.route('/responces', methods=['POST'])
def add_response():
    data = request.get_json()
    name = data['name']
    email = data['email']
    message = data['message']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

    telegram_message = f"Новое сообщение:\nИмя: {name}\nEmail: {email}\nСообщение: {message}"
    send_telegram_message(telegram_message)  # Отправка сообщения в Telegram

    return jsonify({'message': 'Response added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
