from sqlite3 import DatabaseError

from faker import Faker
from random import randint
import sqlite3

fake = Faker('uk-UA')


def generate_and_insert_data_to_db(db_path, count_students, count_groups, count_teachers, count_subjects, count_grade) -> None:

    with sqlite3.connect(db_path) as con:

        cur = con.cursor()

        for _ in range(count_groups):
            cur.execute("INSERT INTO groups (group_name) VALUES (?)",
                        (fake.word(),))

        # Додавання викладачів
        for _ in range(count_teachers):
            cur.execute("INSERT INTO teachers (teacher_name) VALUES (?)",
                        (fake.name(),))

        # Додавання предметів із вказівкою викладача
        for subject_id in range(1, count_teachers + 1):
            for _ in range(int(count_subjects / count_teachers)):
                cur.execute("INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)",
                        (fake.word(), subject_id))

        # Додавання студентів і оцінок
        for group_id in range(1, count_groups + 1):
            for _ in range(int(count_students / count_groups)):
                cur.execute("INSERT INTO students (students_name, group_id) VALUES (?, ?)",
                            (fake.name(), group_id))

                st_id = cur.lastrowid
                for subject_id in range(1, count_subjects + 1):

                    # for _ in range(count_groups):
                    cur.execute(
                        "INSERT INTO grade_book (students_id, subject_id, grade, date_of) VALUES (?, ?, ?, ?)",
                        (st_id, subject_id, randint(0, 100), fake.date_this_decade()))

        try:
            con.commit()
        except DatabaseError:
            con.rollback()
        finally:
            cur.close()
