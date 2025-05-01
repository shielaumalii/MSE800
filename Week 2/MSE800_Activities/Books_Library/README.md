# MSE800 Activities - Week 3
### **Task 1.0:** Library Book Manager
>***Description:***\
>  _A simple program to manage a small library system using object-oriented programming. It allows users to add books and display the current list of available books._
- **_Book Class:_** Class for the identification details (ID) of each book. It initializes and presents the book information such as the book ID number, the title, and the author.
- _**LibraryManager Class:**_ Manages the books in the library. It allows adding a new book to the library and displays all the added books in it. It initializes two attributes: 1) _all_books_ - a dictionary where the keys are book IDS, and 2) _next_id_ - tracks the next available unique ID for a new book. Aside from initialization, it has two other methods: 1) _add_book(title,author)_ - adds new 'Book' class object, assign it to a unique ID in 'next_id', and add it to the 'all_books' dictionary.2) _display_books()_ - prints the content of 'all_books' dictionary.
- _**main() Function:**_ The entry point of the program. Uses a while loop to display the menu and handle the user choice of action.
- **Line 51-52:** _**if __name__ == "__main__":**_ A switch that decides whether the program should start running or not. It checks if this file is being run directly or if it’s being used by another program.