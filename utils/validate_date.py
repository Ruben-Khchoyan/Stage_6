# Функция для проверки соответствия введенный даты требуемым форматам
def validate_date(date_str):
    # Импорт модуля datetime
    from datetime import datetime as dt

    try:
        dt.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False
# Конец функции проверки введенной даты