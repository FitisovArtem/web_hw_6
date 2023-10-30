import sqlite3


def create_db(file_path_sql, file_path_db):
    # читаємо файл зі скриптом для створення БД
    with open(file_path_sql, 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect(file_path_db) as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)


if __name__ == "__main__":
    create_db('university_database.sql', 'university_database.db')
