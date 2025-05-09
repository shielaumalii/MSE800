from database import create_tables
from user_manager import add_user, view_users, search_user, delete_user, adv_search_user, add_course, view_courses, adv_search_course

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Student Name")
    print("4. Delete User by ID")
    print("5. Advanced Search by Keyword")
    print("6. Add Course")
    print("7. View All Courses")
    print("8. Search Course ID and Student Name") 
    print("9. Exit")
    print("=======================")

def main():
    create_tables()
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            course = input("Enter course: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            id = input("Enter ID to search: ")
            name = input("Enter name to search: ")
            users = adv_search_user(id, name)
            for user in users:
                print(user)
        elif choice == '6':
            course_name = input("Enter course name: ")
            course_unit = int(input("Enter course unit: "))
            add_course(course_name, course_unit)
        elif choice == '7':
            users = view_courses()
            for user in users:
                print(user)
        elif choice == '8':
            course_id = int(input("Enter course ID to search: "))
            user_name = input("Enter user name to search: ")
            courses = adv_search_course(course_id, user_name)
            print("\nCourse Search Results:")
            for course in courses:
                print(course)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
