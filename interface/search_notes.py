
# Начало функции поиска
def search_notes(notes, keyword=None, status=None):

    # Импорт модуля termtables (просто нравиться формат вывода)
    import termtables as tt

    # Кортеж возможных статусов заметок
    lst_status_values = ('новая', 'в процессе', 'выполнено')

    # Кортеж ключей для поиска по ключевым словам
    lst_keys = ('username', 'title', 'content')

    # Кортеж для вывода таблицы заметок
    type_info = ('№', 'Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн')

    # Список нужных индексов заметок
    lst_note_index = []

    # Входная информация как можно осуществлять поиск
    print("Поиск заметок можно осуществлять по ключевым словам, по статусу или по ключевым словам и статусу вместе.")

    # Начало цикла проверящий на наличие заметок в списке
    while len(notes) != 0:

        # Цикл ввода и проверки введенных ключевых слов
        while True:
            # Список ключевых слов
            keyword = input("Введите ключевые слова через запятую или "
                            "нажмите Enter чтобы пропустить: ").strip().lower().split(',') # Ввод ключевых слов через запятую
            if '' in keyword:
                keyword = []
                print("Не введены ключевые слова!")
                break
            if len(keyword) != 0:
                break


        # Цикл ввода и проверки статуса заметки
        while True:
            # Статус заметки
            status = input("Введите номер статус заметки или нажмите Enter чтобы пропустить "
                           "(1 -> новая, 2 -> в процессе, 3 -> выполнено): ").strip()
            if status.isdigit() and int(status.strip()) - 1 in range(len(lst_status_values)):
                status = lst_status_values[int(status.strip()) - 1]
                break
            elif status == '':
                print("Статус заметки не выбран!")
                break
            else:
                print("Введен неверный номер статуса заметки!")
                continue


        # Условный оператор вывода информации если нет ключевых и не выбран статус
        if len(keyword) == 0 and status not in lst_status_values:
            print("Не введены ключевые слова и не выбран статус!\n"
                  "Поиск завершен!")


        # Поиск только по статусу
        elif len(keyword) == 0 and status in lst_status_values:
            for i, note in enumerate(notes):
                if status in note.get('status').lower():
                    if i not in lst_note_index:
                        lst_note_index.append(i)


        # Поиск по ключевым словам и статусу
        elif len(keyword) >= 1 and status in lst_status_values:
            for k in keyword:
                if status in lst_status_values: # с выбранным статусом
                    for i, note in enumerate(notes):
                        for j in lst_keys:
                            if k.strip() in note.get(j).lower() and status in note.get('status').lower():
                                if i not in lst_note_index:
                                    lst_note_index.append(i)


        # Поиск по ключевым словам и без статуса
        elif len(keyword) >= 1 and status not in lst_status_values:
            for k in keyword:
                for i, note in enumerate(notes):
                    for j in lst_keys:
                        if k.strip() in note.get(j).lower():
                            if i not in lst_note_index:
                                lst_note_index.append(i)


        # Вывод всех подходящих заметок в виде таблицы
        if len(lst_note_index) > 1:
            print('Найдены следующие заметки:')
            for i, v in enumerate(lst_note_index):
                lst_note_index[i] = [i + 1] + list(notes[v].values())
            print(tt.to_string(lst_note_index, header=type_info))
            break

        elif len(lst_note_index) == 1:
            print('Найдена следующая заметка:')
            lst_note_index[0] = [1] + list(notes[lst_note_index[0]].values())
            print(tt.to_string(lst_note_index, header=type_info))
            break

        else:
            print("Введенные данные не соответствуют ни одной заметке!")
            break


    else: # Вывод информации если список заметок пуст
        print("Список заметок пуст!")
# Конец функции поиска