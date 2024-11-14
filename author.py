class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def add_author(self, name, biography):
        return Author(name, biography)

    def view_author(self):
        return f"Author: {self.name}, Biography: {self.biography}"

    def display_authors(self, authors):
        for author in authors:
            print(author.view_author())
