const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');
const cors = require('cors');

// Создаем сервер
const app = express();
const port = 3306;

// Настройка парсинга JSON данных
app.use(bodyParser.json());
app.use(cors());
// Создание соединения с базой данных MySQL
const db = mysql.createConnection({
  host: 'localhost',       // Имя хоста (например, localhost)
  user: 'root',            // Имя пользователя базы данных
  password: '',            // Пароль базы данных
  database: 'contact_form' // Имя базы данных
});

// Проверка соединения с базой данных
db.connect((err) => {
  if (err) {
    console.error('Ошибка подключения к базе данных: ' + err.stack);
    return;
  }
  console.log('Подключено к базе данных MySQL');
});

// API для отправки формы
app.post('/send-message', (req, res) => {
  const { name, email, message } = req.body;

  // Проверка, что все данные присутствуют
  if (!name || !email || !message) {
    return res.status(400).json({ error: 'Все поля должны быть заполнены' });
  }

  // Запрос на добавление данных в базу
  const query = 'INSERT INTO messages (name, email, message) VALUES (?, ?, ?)';
  db.query(query, [name, email, message], (err, result) => {
    if (err) {
      console.error('Ошибка при добавлении записи: ' + err.stack);
      return res.status(500).json({ error: 'Ошибка сервера' });
    }
    res.status(200).json({ message: 'Заявка успешно отправлена' });
  });
});

// Запуск сервера
app.listen(port, () => {
  console.log(`Сервер работает на порту ${port}`);
});
