# Импорт модуля unittest
import unittest

# Импорт модуля os
import os

# Импорт из database все функции с операциями в базе данных
from database import (setup_database, save_note_to_db, load_notes_from_db,
                              update_note_in_db, delete_note_from_db,
                              search_notes_by_keyword, filter_notes_by_status)

class TestNoteManager(unittest.TestCase):

    test_db = "notes.db"

    # Список заметок
    notes = [{'username': 'Алексей',
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

    # Функция создания базы данных
    def create_note_database(self):

        setup_database(self.test_db)

        for i in self.notes:
            save_note_to_db(i, self.test_db)

    # Функция удаления базы данных если она существует
    def delete_database(self):

        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    # Тестирование сохранения и загрузки заметок из базы данных
    # путем сравнения списка заметок notes и сохраненного, после загруженного из базы данных
    # списка заметок
    def test_save_and_load_note_in_database(self):

        self.create_note_database()

        ls_notes = load_notes_from_db(self.test_db)
        for i in ls_notes:
            i.pop('id')

        self.assertTrue(self.notes == ls_notes)

        self.delete_database()

    # Тестирование функции обновления заметок путем
    # сравнения информации для обновления note_update и обновленной заметки
    def test_note_update(self):

        self.create_note_database()

        note_id = 3

        note_update = {'title': 'Карнавал',
                      'content': 'Купить костюм',
                      'status': 'новая',
                      'issue_date': '23-12-2025'}

        update_note_in_db(note_id, note_update, self.test_db)

        ls_notes_2 = load_notes_from_db(self.test_db)[note_id - 1]
        for i in ('id', 'username', 'created_date'):
            ls_notes_2.pop(i)
        print(ls_notes_2)

        self.assertTrue(note_update == ls_notes_2)

        self.delete_database()

    # Тестирование функции удаления заметок по id
    # путем сравнения id удаленной заметки и списка id всех заметок после удаления
    def test_note_delete(self):

        self.create_note_database()

        num_id = 5

        delete_note_from_db(num_id, self.test_db)

        ls_notes = load_notes_from_db(self.test_db)

        ls_id = []
        for i in ls_notes:
            ls_id.append(i["id"])

        self.assertTrue(num_id not in ls_id)

        self.delete_database()

    # Тестирование функции поиска заметок по ключевому слову.
    # В данном тесте происходит сравнение длины списка заметок,
    # найденнных по ключевому слову в базе данных и
    # количества заметок найденных в списке notes
    # по ключевому слову через цикл for и условный оператор if
    def test_note_search(self):

        self.create_note_database()

        keyword = 'продук'

        ls_notes = search_notes_by_keyword(keyword, self.test_db)

        counter = 0

        for i in self.notes:
            counter += 1 if keyword in i["title"] or keyword in i['content'] else 0

        self.assertTrue(counter == len(ls_notes))

        self.delete_database()

    # Тестирование функции поиска заметок по статусу.
    # В данном тесте происходит сравнение длины списка заметок,
    # найденнных по статусу в базе данных и
    # количества заметок найденных в списке notes
    # по статусу через цикл for и условный оператор if
    def test_note_status_search(self):

        self.create_note_database()

        status_ = 'нов'

        ls_notes = filter_notes_by_status(status_, self.test_db)

        counter = 0

        for i in self.notes:
            counter += 1 if status_ in i["status"] else 0

        self.assertTrue(counter == len(ls_notes))

        self.delete_database()



if __name__ == '__main__':

    unittest.main()