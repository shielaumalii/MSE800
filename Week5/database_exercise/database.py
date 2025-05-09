import sqlite3

def create_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_tables():
    conn_users = create_connection("users.db")
    cursor_users = conn_users.cursor()
    cursor_users.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn_users.commit()
    conn_users.close()

  
    conn_courses = create_connection("course.db")
    cursor_courses = conn_courses.cursor()
    cursor_courses.execute('''
        CREATE TABLE IF NOT EXISTS course (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            course_unit INTEGER NOT NULL
        )
    ''')
    conn_courses.commit()
    conn_courses.close()