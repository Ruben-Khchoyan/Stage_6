from colorama import Fore, Style


def display_notes_with_colors(notes):
    print("\n=== Список заметок ===")

    for note in notes:
        if note['status'] == 'Важная':
            print(Fore.RED + f"• {note['title']}" + Style.RESET_ALL)

        elif note['status'] == 'Выполненная':
            print(Fore.GREEN + f"• {note['title']}" + Style.RESET_ALL)
        else:
            print(Fore.BLUE + f"• {note['title']}" + Style.RESET_ALL)

if __name__ == "__main__":
    # Пример списка заметок
    notes = [
        {"title": "Купить продукты", "status": "Важная"},
        {"title": "Позвонить другу", "status": "Выполненная"},
        {"title": "Прочитать книгу", "status": "Новая"},
    ]
    display_notes_with_colors(notes)