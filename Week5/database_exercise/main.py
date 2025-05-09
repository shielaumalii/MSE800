from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, adv_search_user

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Advanced Search by Keyword")
    print("6. Exit")
    print("=======================")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
