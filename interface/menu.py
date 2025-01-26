
# Начало функции
def menu(notes):
    from colorama import Fore

    from create_note import create_note
    from delete_note import del_note
    from search_notes import search_notes
    from update_note import update_note
    from display_notes import display_notes
    from display_title_notes import display_title_notes

    while True:

        print(Fore.GREEN + '\nМеню действий:',
            Fore.YELLOW + '\n1. Создать новую заметку',
            Fore.BLUE + '\n2. Показать все заметки',
            Fore.MAGENTA + '\n3. Обновить заметку',
            Fore.RED + '\n4. Удалить заметку',
            Fore.CYAN + '\n5. Найти заметки',
            Fore.BLUE + '\n6. Выйти из программы')
        solve = input(Fore.GREEN + '\nНапишите номер одного из действий: ').strip()


        if solve == '1':
            notes.append(create_note())
            print("Заметка создана!")
            display_notes(notes)
            continue


        elif solve == '2':
            while True:

                if len(notes) == 0:
                    print('\nУ вас нет сохранённых заметок.')
                    break

                create_new_note = input("1 -> вывести только заголовки заметок\n"
                                        "2 -> вывести полностью данные\n"
                                        "Выберите уровень детализации: ")

                if create_new_note.strip().lower() == '1':
                    display_title_notes(notes)
                    break

                elif create_new_note.strip().lower() == '2':
                    display_notes(notes)
                    break

                else:  # Если не правильный ответ, то цикл while повторяется
                    print('\nНе корректный ответ!\n')
                    continue
            continue


        elif solve == '3':
            # Цикл для изменения заметок вызовом функции update_note. В случае отказа цикл завершается.
            while len(notes) >= 1:
                question = input("\nЖелаете изменить данные заметки? (да/нет): ")
                if question.strip().lower() not in ['да',
                                                    'нет']:  # Условный оператор выводящий замечание если не правильно дан ответ на вопрос
                    print('\nНе корректный ответ!')
                elif question.strip().lower() == 'да':
                    display_notes(notes)
                    note_num = input('\nВыберите номер заметки, которую хотите изменить: ').strip()
                    if note_num.isdigit() and int(note_num) in range(
                            len(notes) + 1):  # Проверка введенного номера заметки в списке заметок
                        update_note(notes[int(note_num) - 1])
                    else:  # Выводит замечание если заметки с таким номером не существует
                        print("\nВведен неверный номер заметки!")
                elif question.strip().lower() == 'нет':  # Если изменения заметкам не требуется или больше изменений не требуется, то выводиться актуальный список заметок
                    display_notes(notes)
                    break
                display_notes(notes)
            else:
                print("Список заметок пуст!")
            continue


        elif solve == '4':
            del_note(notes)
            continue


        elif solve == '5':
            search_notes(notes)
            continue


        elif solve == '6':
            break


        else:
            print("Неверный выбор. Пожалуйста, выберите действие из меню.")
            continue
    print('Программа завершена. Спасибо за использование!')
# Конец функции


if __name__ == '__main__':
    # Список с несколькими заметками
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

    # Список с одной заметкой
    lst_notes_1 = [{'username': 'Алексей',
                  'title': 'Список дел',
                  'content': 'Купить продукты на неделю',
                  'status': 'новая',
                  'created_date': '18-11-2024',
                  'issue_date': '19-11-2024'}]

    # Пустой список заметок
    lst_notes_2 = []


    menu(lst_notes_2)