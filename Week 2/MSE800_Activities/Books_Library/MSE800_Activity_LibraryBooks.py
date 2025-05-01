class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __repr__(self):
        return f"\nBook ID: {self.book_id} \nTitle: {self.title} \nAuthor: {self.author}"


class LibraryManager:
    def __init__(self):
        self.all_books = {} 
        self.next_id = 1001 

    def add_book(self, title, author):
        book = Book(self.next_id, title, author)
        self.all_books[self.next_id] = book
        self.next_id += 1
        print("Book added successfully!")

    def display_books(self):
        if not self.all_books:
            print("No books in the library yet.")
        else:
            for book in self.all_books.values():
                print(book)

def main():
    library = LibraryManager()
    while True: 
        print("\nLibrary Menu:")
        print("1. Add a Book")
        print("2. Display All Books")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            library.add_book(title, author)
        elif choice == "2":
            print("\nBooks in the Library:")
            library.display_books()
        elif choice == "3":
            print("Exiting the library manager...")
            break
        else:
            print("Invalid. Type 1, 2, or 3 to continue...")

if __name__ == "__main__":
    main()
