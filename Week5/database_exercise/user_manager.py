from database import create_connection
import sqlite3

def add_user(name, email):

    conn_courses = create_connection("course.db")
    cursor_courses = conn_courses.cursor()
    cursor_courses.execute("SELECT course_id, course_name FROM course")
    courses = cursor_courses.fetchall()

    if not courses:
        print("No courses available. Please add courses first.")
        conn_courses.close()
        return

    print("\nAvailable Courses:")
    for course in courses:
        print(f"{course[0]}: {course[1]}")

    try:
        course_id = int(input("\nEnter the course ID to assign to the user: "))
        selected_course = next((course for course in courses if course[0] == course_id), None)
        if not selected_course:
            print("Invalid course ID. User not added.")
            conn_courses.close()
            return
    except ValueError:
        print("Invalid input. Please enter a valid course ID.")
        conn_courses.close()
        return

    conn_courses.close()

    conn_users = create_connection("users.db")
    cursor_users = conn_users.cursor()
    try:
        cursor_users.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn_users.commit()
        print(f"User added successfully to users.db and assigned to course: {selected_course[1]}")
    except sqlite3.IntegrityError:
        print("Email must be unique.")
    finally:
        conn_users.close()

def view_users():
    conn = create_connection("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("\n No user yet.")
        return []
    
    return rows


def search_user(name):
    conn = create_connection("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_user(user_id):
    conn = create_connection("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")


def adv_search_user(id, name):
    conn = create_connection("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ? AND id = ?", ('%' + name + '%', id))
    rows = cursor.fetchall()
    conn.close()
    return rows


def add_course(course_name, course_unit):
    conn = create_connection("course.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course (course_name, course_unit) VALUES (?, ?)", (course_name, course_unit))
        conn.commit()
        print("Course added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding course: {e}")
    conn.close()

def view_courses():
    conn = create_connection("course.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    conn.close()
    return rows

def adv_search_course(course_id, user_name):
    conn_users = create_connection("users.db")
    conn_courses = create_connection("course.db")
    cursor_users = conn_users.cursor()
    cursor_courses = conn_courses.cursor()

   
    cursor_users.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + user_name + '%',))
    user = cursor_users.fetchone()

    if user:
        cursor_courses.execute("SELECT * FROM course WHERE course_id = ?", (course_id,))
        course = cursor_courses.fetchone()
        conn_users.close()
        conn_courses.close()
        if course:
            return [(course, user)]
        else:
            print("Course not found.")
            return []
    else:
        print("User not found.")
        conn_users.close()
        conn_courses.close()
        return []