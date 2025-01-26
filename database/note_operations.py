# Импорт модуля sqlite3
import sqlite3


# Начало функции сохранения заметок в базе данных
def save_note_to_db(note, db_path):

    # Подключение к базе данных
    connection = sqlite3.connect(db_path)

    # Создание объекта курсора для выполнения команд SQL
    cursor = connection.cursor()


    # Внесение заметки в таблицу заметок
    cursor.execute("""

        INSERT INTO notes (username, title, content, status, created_date, issue_date)

        VALUES (?, ?, ?, ?, ?, ?);

    """, (note['username'],
          note['title'],
          note['content'],
          note['status'],
          note['created_date'],
          note['issue_date']))


    # Сохранение
    connection.commit()

    # Закрытие и прекращение работы с базой данных
    connection.close()
# Конец функции сохранения заметок в базе данных


# Начало функции выгрузки заметок из таблицы
def load_notes_from_db(db_path):

    # Подключение к базе данных
    connection = sqlite3.connect(db_path)

    # Создание объекта курсора для выполнения команд SQL
    cursor = connection.cursor()


    # Выбор заметок из таблицы заметок
    cursor.execute("SELECT * FROM notes")


    # Получение всех заметок
    rows = cursor.fetchall()


    # Создания списка с заметками в виде словарей
    notes = [{

            'id': row[0],

            'username': row[1],

            'title': row[2],

            'content': row[3],

            'status': row[4],

            'created_date': row[5],

            'issue_date': row[6],

        } for row in rows]

    # Закрытие и прекращение работы с базой данных
    connection.close()

    # Возвращение списка с заметками
    return notes
# Конец функции выгрузки заметок из таблицы


# Начало функции обновления заметок
def update_note_in_db(note_id, updates, db_path):

    # Подключение к базе данных
    connection = sqlite3.connect(db_path)

    # Создание объекта курсора для выполнения команд SQL
    cursor = connection.cursor()


    # Обновление заголовков, описания, статуса и дедлайна заметки по номеру id
    cursor.execute("""

        UPDATE notes

        SET title = ?, content = ?, status = ?, issue_date = ?

        WHERE id = ?;

    """, (updates['title'], updates['content'], updates['status'], updates['issue_date'], note_id))


    # Сохранение
    connection.commit()

    # Закрытие и прекращение работы с базой данных
    connection.close()
# Конец функции обновления заметок


# Начало функции удаления заметки по id
def delete_note_from_db(note_id, db_path):

    # Подключение к базе данных
    connection = sqlite3.connect(db_path)

    # Создание объекта курсора для выполнения команд SQL
    cursor = connection.cursor()


    # Удаление заметки из таблицы заметок по id
    cursor.execute("DELETE FROM notes WHERE id = ?;", (note_id,))


    # Сохранение
    connection.commit()

    # Закрытие и прекращение работы с базой данных
    connection.close()
# Конец функции удаления заметки по id


# Начало функции поиска по ключевому слову
def search_notes_by_keyword(keyword, db_path):

    # Подключение к базе данных
    connection = sqlite3.connect(db_path)

    # Создание объекта курсора для выполнения команд SQL
    cursor = connection.cursor()


    # Выбор заметок из таблицы по ключевому слову совпадающему с заголовками или описаниями
    cursor.execute("""

        SELECT * FROM notes

        WHERE title LIKE ? OR content LIKE ?;

    """, (f"%{keyword}%", f"%{keyword}%"))


    # Получение списка с соответствующими заметками
    rows = cursor.fetchall()

    # Закрытие и прекращение работы с базой данных
    connection.close()


    # Возвращение списка с соответствующими заметками в виде словарей
    return [{'id': row[0],
             'username': row[1],
             'title': row[2],
             'content': row[3],
             'status': row[4],
             'created_date': row[5],
             'issue_date': row[6]} for row in rows]
# Конец функции поиска по ключевому слову


# Начало функции вывода заметок по статусу
def filter_notes_by_status(status, db_path):

    # Подключение к базе данных
    connection = sqlite3.connect(db_path)

    # Создание объекта курсора для выполнения команд SQL
    cursor = connection.cursor()


    # Выбор заметок по статусу
    cursor.execute("""

        SELECT * FROM notes WHERE status LIKE ?;

    """, (f'%{status}%',))


    # Получение списка с соответствующими заметками
    rows = cursor.fetchall()

    # Закрытие и прекращение работы с базой данных
    connection.close()


    # Возвращение списка заметок в виде словарей с выбранным статусом
    return [{'id': row[0],
             'username': row[1],
             'title': row[2],
             'content': row[3],
             'status': row[4],
             'created_date': row[5],
             'issue_date': row[6]} for row in rows]
# Конец функции вывода заметок по статусу



if __name__ == '__main__':

    ls_notes = [{'username': 'Алексей',
                  'title': 'Список покупок',
                  'content': 'Купить продукты на неделю',
                  'status': 'новая',
                  'created_date': '27-11-2024',
                  'issue_date': '30-11-2024'},

                 {'username': 'Мария',
                  'title': 'Учеба',
                  'content': 'Подготовиться к экзамену',
                  'status': 'в процессе',
                  'created_date': '25-11-2024',
                  'issue_date': '01-12-2024'},

                 {'username': 'Иван',
                  'title': 'План работы',
                  'content': 'Завершить проект',
                  'status': 'выполнено',
                  'created_date': '20-11-2024',
                  'issue_date': '26-11-2024'},

                 {'username': 'Дима',
                  'title': 'Список покупок',
                  'content': 'Купить продукты на неделю',
                  'status': 'новая',
                  'created_date': '27-11-2024',
                  'issue_date': '30-11-2024'},

                 {'username': 'Лена',
                  'title': 'Учеба',
                  'content': 'Подготовиться к экзамену',
                  'status': 'в процессе',
                  'created_date': '25-11-2024',
                  'issue_date': '01-12-2024'},

                 {'username': 'Петр',
                  'title': 'План работы',
                  'content': 'Завершить проект',
                  'status': 'выполнено',
                  'created_date': '20-11-2024',
                  'issue_date': '26-11-2024'}
                 ]
    #
    # for i in range(len(ls_notes)):
    #     save_note_to_db(ls_notes[i],"notes.db")


    # note_1 = load_notes_from_db("notes.db")
    #
    # for i in note_1:
    #     i.pop('id')
    #
    # from interface import display_notes
    # display_notes(note_1)


    # notes_2 = [{'username': 'Петя',
    #           'title': 'Список овощей',
    #           'content': 'Купить грибы и помидоры',
    #           'status': 'в процессе',
    #           'created_date': '01-11-2024',
    #           'issue_date': '30-11-2024'}]
    # update_note_in_db(10, notes_2[0],"notes.db")

    # for i in range(3435):
    #     delete_note_from_db(i, 'notes.db')

    # note_1 = search_notes_by_keyword('продук','notes.db')
    # for i in range(len(note_1)):
    #     print(note_1[i])

    # note_2 = filter_notes_by_status('нова', 'notes.db')
    # for i in range(len(note_2)):
    #     print(note_2[i])