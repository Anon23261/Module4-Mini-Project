from book import Book
from user import User
from author import Author
import error_handler

def display_menu():
    print("\nWelcome to the Library Management System!")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")

def book_operations(books):
    while True:
        try:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Return to main menu")
            choice = input("Choose an option: ")

            if choice == "6":
                break

            if choice not in ["1", "2", "3", "4", "5"]:
                error_handler.handle_invalid_input()
                continue

            if choice == "1":
                title = input("Enter title: ").strip()
                author = input("Enter author: ").strip()
                genre = input("Enter genre: ").strip()
                pub_date = input("Enter publication date (YYYY-MM-DD): ").strip()
                
                if not all([title, author, genre, pub_date]):
                    print("All fields are required!")
                    continue
                
                if not error_handler.validate_input(r'^\d{4}-\d{2}-\d{2}$', pub_date):
                    print("Invalid date format! Please use YYYY-MM-DD")
                    continue

                new_book = Book(title, author, genre, pub_date)
                books.append(new_book)
                print("Book added successfully.")

            elif choice in ["2", "3", "4"]:
                title = input("Enter the book title: ").strip()
                if not title:
                    print("Title cannot be empty!")
                    continue
                
                for book in books:
                    if book.title.lower() == title.lower():
                        if choice == "2":
                            print(book.borrow_book())
                        elif choice == "3":
                            print(book.return_book())
                        else:
                            print(book.display_book_info())
                        break
                else:
                    print("Book not found.")

            elif choice == "5":
                if not books:
                    print("No books in the library.")
                else:
                    for book in books:
                        print(book.display_book_info())
                        
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def user_operations(users):
    print("\nUser Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        new_user = User(name, library_id)
        users.append(new_user)
        print("User added successfully.")

    elif choice == "2":
        library_id = input("Enter user ID to view details: ")
        for user in users:
            if user.library_id == library_id:
                print(user.view_user())
                break
        else:
            print("User not found.")

    elif choice == "3":
        for user in users:
            print(user.view_user())

def author_operations(authors):
    print("\nAuthor Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter author name: ")
        biography = input("Enter biography: ")
        new_author = Author(name, biography)
        authors.append(new_author)
        print("Author added successfully.")

    elif choice == "2":
        name = input("Enter author name to view details: ")
        for author in authors:
            if author.name.lower() == name.lower():
                print(author.view_author())
                break
        else:
            print("Author not found.")

    elif choice == "3":
        for author in authors:
            print(author.view_author())

def main():
    books = []
    users = []
    authors = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            book_operations(books)
        elif choice == "2":
            user_operations(users)
        elif choice == "3":
            author_operations(authors)
        elif choice == "4":
            print("Thank you for using the Library Management System!")
            break
        else:
            error_handler.handle_invalid_input()

if __name__ == "__main__":
    main()
