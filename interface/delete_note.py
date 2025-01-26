
from display_notes import display_notes

# Функция для удаления заметок note по ключевым словам word
def del_note(notes):

    ind_del_note = [] # Список с индексами заметок которые требуется удалить

    # Импорт модуля termtables (просто нравиться формат вывода)
    import termtables as tt

    type_info = ['№', 'Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн']

    # Цикл для удаления заметок при желании удалить заметки и их наличии в списке
    while len(notes) != 0:

        del_solve = input('Желаете удалить заметки? (да/нет): ')
        if del_solve not in ['да', 'нет']:
            print('\nНе корректный ответ!\n')
            continue
        elif del_solve == 'да':
            display_notes(notes)

            while True:
                word = input('Введите имя пользователя или заголовок для удаления заметки: ').strip().lower()
                if word == '':
                    print('\nНе введены имя пользователя или заголовок для удаления заметки!\n')
                    continue

                else:
                    # Цикл для прохождения по всем элементам списка с заметками
                    for i in range(len(notes)):

                        # Условный оператор для проверки входимости ключевых слов в имя пользователя или заголовки
                        if word in notes[i]['username'].lower() or word.strip().lower() in notes[i]['title'].lower():
                            print(tt.to_string([list(notes[i].values())],header=type_info[1:]))  # Вывод таблицы с полной информацией

                            # Цикл для уточнения информации об удалении заметки.
                            # Если да то номер индекса добавляется в список ind_del_note
                            while True:
                                solve = input("Вы уверены, что хотите удалить заметку? (да/нет): ").strip().lower()
                                if solve == 'да':
                                    ind_del_note.append(i)
                                    break
                                elif solve == 'нет':
                                    print('Заметка не удалена!')
                                    break
                                else:
                                    print('\nНе корректный ответ!\n')
                                    continue
                break


            if len(ind_del_note) >= 1:
                # Цикл для удаления заметок по индексам из списка ind_del_note в обратном порядке чтобы не было ошибки
                for i in ind_del_note[::-1]:
                    notes.pop(i)
                    print('\nЗаметка успешно удалена.')
                # Вывод заметок после удаления
                if len(notes) == 1:
                    print('\nОсталась одна заметка:')
                    display_notes(notes)
                elif len(notes) > 1:
                    print('\nОстались следующие заметки:')
                    display_notes(notes)
                elif len(notes) == 0:
                    print('\nСписок заметок пуст!')
            else:
                print('\nЗаметок с таким именем пользователя или заголовком не найдено или заметки не удалены.')

            break
        elif del_solve == 'нет':
            break
    else:
        print("\nCписок заметок пуст.")
# Конец функции


if __name__ == "__main__":
    lst_notes = [{'username': 'Игорь',
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

    del_note(lst_notes)