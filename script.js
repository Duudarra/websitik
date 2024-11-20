// Находим все кнопки и вкладки
const buttons = document.querySelectorAll('.tab-button');
const tabs = document.querySelectorAll('.tab-content');

// Добавляем обработчики кликов на кнопки
buttons.forEach(button => {
    button.addEventListener('click', () => {
        // Убираем класс "active" со всех кнопок
        buttons.forEach(btn => btn.classList.remove('active'));
        // Добавляем "active" на кликнутую кнопку
        button.classList.add('active');
        
        // Скрываем все вкладки
        tabs.forEach(tab => tab.classList.remove('active'));
        // Показываем соответствующую вкладку
        const tabId = button.getAttribute('data-tab');
        document.getElementById(tabId).classList.add('active');
    });
});

// Находим все элементы с целями
const goalItems = document.querySelectorAll('.goal-item');
const goalsSection = document.getElementById('goals');

// Обработчик наведения на элементы с целями
goalItems.forEach(item => {
    item.addEventListener('mouseover', () => {
        // Получаем путь к фону, который должен отображаться
        const imageSrc = item.getAttribute('data-image'); // Путь к изображению
        // Меняем фон контейнера с целями
        goalsSection.style.backgroundImage = `url('${imageSrc}')`;
    });

    // При уходе с элемента, восстанавливаем фон по умолчанию
    item.addEventListener('mouseout', () => {
        goalsSection.style.backgroundImage = ''; // Убираем фоновое изображение
    });
});
