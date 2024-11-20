from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

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

    responses = []
    for row in rows:
        responses.append({'id': row['id'], 'name': row['name'], 'email': row['email'], 'message': row['message']})

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
    cursor.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
                   (name, email, message))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Response added successfully!'}), 201

@app.route('/')
def index():
    return get_responses()

if __name__ == '__main__':
    app.run(debug=True)
