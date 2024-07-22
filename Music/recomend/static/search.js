// Получаем поле ввода для поиска
const searchInput = document.getElementById('search-input');

searchInput.addEventListener('input', function() {
    const userInput = searchInput.value;

    fetch(`/search_suggestions/?query=${userInput}`)
        .then(response => response.json())
        .then(data => {
            clearSuggestions();
            if(userInput) {
                data.forEach(suggestion => {
                    const suggestionElement = document.createElement('div');
                    suggestionElement.innerHTML = `<a href="/song/${suggestion.id}">${suggestion.title} - ${suggestion.artist}</a>`;
                    document.getElementById('suggestions-container').appendChild(suggestionElement);

                });
                document.getElementById('suggestions-container').style.display = 'block'; // Показывать suggestions-container, если есть ввод
            } else {
                document.getElementById('suggestions-container').style.display = 'none'; // Скрывать suggestions-container, если текстовое поле пустое
            }
        });
});



// Добавляем обработчик события для отслеживания ввода пользователя
searchInput.addEventListener('keyup', function() {
    const userInput = searchInput.value; // Получаем то, что ввел пользователь

    // Делаем AJAX-запрос к представлению Django для получения подсказок
    fetch(`/search_suggestions/?query=${userInput}`)
        .then(response => response.json())
        .then(data => {
            // Очищаем предыдущие подсказки
            clearSuggestions();

            // Отображаем полученные подсказки
            data.forEach(suggestion => {
                const suggestionElement = document.createElement('div');
                suggestionElement.innerHTML = `<a href="/song/${suggestion.id}">${suggestion.title} - ${suggestion.artist}</a>`;
                // Добавляем созданную подсказку к DOM
                document.getElementById('suggestions-container').appendChild(suggestionElement);
            });
        });
});

// Функция для очистки предыдущих подсказок
function clearSuggestions() {
    document.getElementById('suggestions-container').innerHTML = '';
}

