# Начало функции добавления в файл с заметками заметки в формате JSON
def save_notes_json(notes, filename):

    # Импорт модуля json
    import json

    # Кортеж с ключами отображающими смысл данных на русском
    keys = ('Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн')

    # Создание нового списка заметок с ключами из keys.
    # Для создания словаря с нужными ключами используется функция zip,
    # которой передается ключи и список значений заметки из словаря.
    # И так для каждой заметки через цикл for
    new_lst_notes = list(dict(zip(keys, note.values())) for note in notes)

    # Начало блока try для обработки ошибок
    try:
        # Открытие файла через оператор with, чтобы исключить строку с закрытием файла.
        # encoding='UTF-8', кодировка для работы с русским языком.
        # 'w' - перезапись или создание файла с заметками
        # Функция file.write() для записи заметок в файл
        # json.dumps - преобразования списка в строку в json формате
        # ensure_ascii=False - отключение данного параметра позволяет использовать кодировку UTF-8
        # indent=4 - отступ в 4 пробела для читабельности файла
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write(json.dumps(new_lst_notes, ensure_ascii=False, indent=4))
    except UnicodeDecodeError: # Обработка ошибки чтения файла.
        print('Ошибка при чтении файла. Проверьте его содержимое.')
    except PermissionError: # Обработка ошибки доступа к файлу
        print('Ошибка доступа! Отсутствие прав доступа!')
# Конец функции