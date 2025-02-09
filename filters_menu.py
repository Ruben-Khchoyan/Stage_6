def filter_notes(notes, filter_type, filter_value):
    if filter_type == "keyword":
        return [note for note in notes if filter_value.lower() in
                note['title'].lower()]
    elif filter_type == "status":
        return [note for note in notes if note['status'] ==
                filter_value]
    elif filter_type == "date":
        return [note for note in notes if note['date'] ==
                filter_value]
    else:
        return notes


def filters_menu(notes):
    print("\n=== Фильтры ===")
    print("1. По ключевому слову")
    print("2. По статусу (Важная, Выполненная, Новая)")
    print("3. По дате")
    choice = input("Выберите фильтр: ")

    if choice == "1":
        keyword = input("Введите ключевое слово: ")
        filtered_notes = filter_notes(notes, "keyword", keyword)
    elif choice == "2":
        status = input("Введите статус (Важная/Выполненная/Новая):")
        filtered_notes = filter_notes(notes, "status", status)
    elif choice == "3":
        date = input("Введите дату (формат: ГГГГ-ММ-ДД): ")
        filtered_notes = filter_notes(notes, "date", date)
    else:
        print("Ошибка: Некорректный выбор фильтра.")
        return

    if filtered_notes:
        for note in filtered_notes:
            print(f"• {note['title']} ({note['status']}) — {note['date']}")
    else:
        print("Нет заметок, соответствующих фильтру.")

if __name__ == "__main__":
    # Пример списка заметок
    notes = [
        {"title": "Купить продукты", "status": "Важная", "date":
            "2024-11-27"},
        {"title": "Позвонить другу", "status": "Выполненная",
         "date": "2024-11-26"},
        {"title": "Прочитать книгу", "status": "Новая", "date":
            "2024-11-25"},
    ]
    filters_menu(notes)