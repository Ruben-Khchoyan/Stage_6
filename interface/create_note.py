
# Функция для создания заметок
def create_note():
    # Импорт модуля datetime
    from datetime import datetime as dt

    # Цикл для введения имени пользователя и проверки чтобы не была пустая строка
    while True:
        user_name = input("\nВведите имя пользователя: ")
        if user_name.strip() == '':
            continue
        break


    # Цикл для введения заголовка заметки и проверки чтобы не была пустая строка
    while True:
        title = input("Введите заголовок заметки: ")
        if title.strip() == '':
            continue
        break


    # Цикл для введения описания заметки и проверки чтобы не была пустая строка
    while True:
        content = input("Введите описание заметки: ")
        if content.strip() == '':
            continue
        break


    # Цикл для введения статуса заметки по числам (так быстрее, чем писать статус).
    # Так же есть проверка чтобы введеное число было в диапазоне от 1 до 3.
    while True:
        num_status = input("Введите номер статуса заметки (1 -> новая; 2 -> в процессе; 3 -> выполнено): ")
        lst_status = ['новая', 'в процессе', 'выполнено']
        if num_status.isdigit(): # Проверка что введено число
            if int(num_status) in range(1, len(lst_status)+1):
                status = lst_status[int(num_status)-1].lower()
                break
        print('Статус заметки введен не правильно!')


    # Функция для проверки соответствия введенный даты требуемым форматам
    def data_check(data):
        for fmt in ('%d-%m-%Y', ):
            try:
                return dt.strptime(data, fmt)
            except ValueError:
                pass
        else:
            print('Введен неверный формат данных!')
            return 0
    # Конец функции проверки введенной даты


    # Цикл для ввода дедлайна заметки. Дата создания автоматически является текущий день
    # Через if и функцию check проверятся правильность введения формата данных
    while True:
        print(f'Форматы ввода дат:\n ДД-ММ-ГГГГ')


        # Цикл проверки формата ввденной даты создания
        created_date = dt.today()


        # Цикл проверки формата ввденной даты истечения
        issue_date = input("Введите дату дедлайна: ")
        if data_check(issue_date) != 0:
            issue_date = data_check(issue_date)
        else:
            continue


        # Цикл проверки, чтобы дата истечения была позже даты дедлайна
        if issue_date < created_date:
            print("Дата дедлайна не может быть раньше даты создания заметки!")
            continue
        else:
            break


    # Результат вывода фцнкции словарь со всеми данными заметок
    return {'username':user_name,
            'title':title,
            'content':content,
            'status':status,
            'created_date':created_date.strftime('%d-%m-%Y'),
            'issue_date':issue_date.strftime('%d-%m-%Y')}
# Конец функции создания заметок


if __name__ == '__main__':
    # Список со всеми заметками
    lst_notes = []

    # Добавление первой заметки
    lst_notes.append(create_note())


    # Цикл для создания дополнительных заметок. В случае отказа цикл завершается.
    while True:
        create_new_note = input("Хотите добавить ещё одну заметку? (да/нет): ")
        if create_new_note.strip().lower() not in ['да', 'нет']:
            print('\nНе корректный ответ!\n')
        elif create_new_note.strip().lower() == 'да':
            lst_notes.append(create_note())
        elif create_new_note.strip().lower() == 'нет':
            break


    # Вывод всех заметок из списка lst_notes.
    if len(lst_notes) == 0:
        print('Список заметок пуст!')
    elif len(lst_notes) == 1:
        print('Заметка создана:\n', lst_notes[0])
    else:
        print('Заметки созданы:')
        for i in range(len(lst_notes)):
            print(f'{i + 1}. {lst_notes[i]}')