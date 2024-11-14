class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []
        self.borrow_history = []

    def borrow_book(self, book):
        if book.availability:
            book.borrow_book(self)
            self.borrowed_books.append(book)
            self.borrow_history.append({
                'book': book,
                'action': 'borrowed',
                'date': book.borrow_date
            })
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            self.borrow_history.append({
                'book': book,
                'action': 'returned',
                'date': book.return_date
            })
            return True
        return False

    def view_user(self):
        borrowed = [book.title for book in self.borrowed_books]
        return (f"User Information:\n"
                f"Name: {self.name}\n"
                f"Library ID: {self.library_id}\n"
                f"Currently Borrowed Books: {', '.join(borrowed) if borrowed else 'None'}")

    def view_history(self):
        if not self.borrow_history:
            return "No borrowing history"
        
        history = "Borrowing History:\n"
        for record in self.borrow_history:
            history += f"- {record['book'].title}: {record['action']} on {record['date']}\n"
        return history

    def __str__(self):
        return self.view_user()

    def __repr__(self):
        return f"User('{self.name}', '{self.library_id}')"
