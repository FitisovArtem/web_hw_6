from create_db import create_db
import generator_data
import sqlite3

FILE_PATH_SQL = 'university_database.sql'
FILE_PATH_DB = 'university_database.db'
QUERY_PATH = 'query/'
COUNT_STUDENTS = 45
COUNT_TEACHER = 3
COUNT_GROUP = 3
COUNT_SUBJECT = 6
COUNT_GRADE = 20


def execute_query(sql: str, db_path: str) -> list:
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


def read_file(path) -> str:
    with open(path, 'r') as opened_file:
        return opened_file.read()


if __name__ == '__main__':

    create_db(FILE_PATH_SQL, FILE_PATH_DB)
    generator_data.generate_and_insert_data_to_db(FILE_PATH_DB, COUNT_STUDENTS, COUNT_GROUP, COUNT_TEACHER, COUNT_SUBJECT, COUNT_GRADE)

    for i in range(1, 11):
        file = 'query_' + str(i) + '.sql'
        query_from_file = read_file(QUERY_PATH+file)
        result_query = execute_query(query_from_file, FILE_PATH_DB)
        print('Result ' + file + '')
        print(result_query)
        print('\n')

    for i in range(1, 3):
        file = 'query_add_' + str(i) + '.sql'
        query_from_file = read_file(QUERY_PATH+file)
        result_query = execute_query(query_from_file, FILE_PATH_DB)
        print('Result' + file + '')
        print(result_query)
        print('\n')
