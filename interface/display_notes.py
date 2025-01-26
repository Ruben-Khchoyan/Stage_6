
# Начало функции вывода заметок
def display_notes(notes):

    # Импорт модуля termtables (просто нравиться формат вывода)
    import termtables as tt

    # Список с заголовками таблицы вывода
    type_info = ['id', 'Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн']

    # Если количество заметок в списке больше 1
    if len(notes) > 1:
        print('Список заметок:')
        lst_dict_values = [] # Список всех значений
        for i, v in enumerate(notes):  # Цикл вывода списков со всеми значениями
            lst_dict_values.append([i + 1] + list(v.values()))
        print(tt.to_string(lst_dict_values, header=type_info))  # Вывод таблицы с полной информацией

    # Если заметка одна
    elif len(notes) == 1:
        print('Заметка:')
        lst_dict_values = [1] + list(notes[0].values()) # Список всех значений заметки
        print(tt.to_string([lst_dict_values], header=type_info)) # Вывод таблицы с полной информацией
# Конец функции вывода заметок