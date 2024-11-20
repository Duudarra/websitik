from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('contact_form.db')
    conn.row_factory = sqlite3.Row  # Это позволит обращаться к столбцам по имени
    return conn

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

    return jsonify({'message': 'Response added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
