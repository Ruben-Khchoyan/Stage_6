# Импорт модуля sqlite3
import sqlite3

# Начало функции создания базы данных SQL
def setup_database(db_path):

    # Подключение к базе данных
    connection = sqlite3.connect(db_path)

    # Создание объекта курсора для выполнения команд SQL
    cursor = connection.cursor()


    # Создание таблицы notes если ее нет
    cursor.execute("""

        CREATE TABLE IF NOT EXISTS notes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT NOT NULL,

            title TEXT NOT NULL,

            content TEXT NOT NULL,

            status TEXT NOT NULL,

            created_date TEXT NOT NULL,

            issue_date TEXT NOT NULL

        );

    """)

    # Сохранение
    connection.commit()

    # Закрытие и прекращение работы с базой данных
    connection.close()
# Конец функции создания базы данных SQL


# Инициализация базы данных
if __name__ == "__main__":

    setup_database("notes.db")
