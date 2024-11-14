class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability = True
        self.borrower = None
        self.borrow_date = None
        self.return_date = None

    def borrow_book(self, user=None):
        if self.availability:
            self.availability = False
            self.borrower = user
            from datetime import datetime
            self.borrow_date = datetime.now().strftime("%Y-%m-%d")
            return f"'{self.title}' has been borrowed{f' by {user.name}' if user else ''}."
        else:
            return f"'{self.title}' is currently unavailable{f' (borrowed by {self.borrower.name})' if self.borrower else ''}."

    def return_book(self):
        if not self.availability:
            self.availability = True
            from datetime import datetime
            self.return_date = datetime.now().strftime("%Y-%m-%d")
            self.borrower = None
            return f"'{self.title}' has been returned."
        else:
            return f"'{self.title}' was not borrowed."

    def display_book_info(self):
        status = "Available" if self.availability else f"Borrowed{f' by {self.borrower.name}' if self.borrower else ''}"
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Genre: {self.genre}\n"
                f"Published: {self.publication_date}\n"
                f"Status: {status}")

    def __str__(self):
        return self.display_book_info()

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.genre}', '{self.publication_date}')"
