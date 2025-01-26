
# Начало функции вывода заголовков заметок
def display_title_notes(notes):
    # Список с заголовками таблицы вывода
    type_info = ['№', 'Заголовок']

    # Импорт модуля termtables (просто нравиться формат вывода)
    import termtables as tt

    # Если количество заметок в списке больше 1
    if len(notes) > 1:
        print('Список заголовков заметок:')
        lst_dict_titles = []  # Список с заголовками
        for i in range(len(notes)):  # Цикл вывода нужных значений
            lst_dict_titles.append([i + 1] + [notes[i].get('title')])

        print(tt.to_string(lst_dict_titles, header=type_info))  # Вывод таблицы с заголовками

    # Если заметка одна
    elif len(notes) == 1:
        print('Заголовок заметки:')
        lst_dict_values = [1] + [notes[0].get('title')]  # Вывод нужного заголовка
        print(tt.to_string([lst_dict_values], header=type_info))  # Вывод таблицы с заголовком

# Конец функции вывода заголовков заметок