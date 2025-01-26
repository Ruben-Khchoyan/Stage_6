import unittest

from data import save_notes_json, load_notes_from_file

from utils import validate_date, validate_status, generate_unique_id

from interface import menu, display_notes

import os

class TestNoteManager(unittest.TestCase):

    test_file = 'test.json'

    def test_save_and_load_notes(self):

        notes = [{'username': 'Алексей',
                    'title': 'Список дел',
                    'content': 'Купить продукты на неделю',
                    'status': 'новая',
                    'created_date': '18-11-2024',
                    'issue_date': '19-11-2024'},

                   {'username': 'Петя',
                    'title': 'Список овощей',
                    'content': 'Купить грибы и помидоры',
                    'status': 'в процессе',
                    'created_date': '01-11-2024',
                    'issue_date': '30-11-2024'},

                   {'username': 'Илья',
                    'title': 'Починить машину',
                    'content': 'Купить клапана и свечи',
                    'status': 'новая',
                    'created_date': '04-11-2024',
                    'issue_date': '20-11-2024'}]

        save_notes_json(notes, self.test_file)

        loaded_notes = load_notes_from_file(self.test_file)

        self.assertIsNone(display_notes(loaded_notes))

        self.assertEqual(notes, loaded_notes)

        self.assertTrue(validate_date('12-12-1212'))

        self.assertTrue(validate_status('в процессе'))

        self.assertTrue(generate_unique_id())

        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':

    unittest.main()