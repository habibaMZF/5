class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn      # private
        self.available = True

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available: {self.available}")

    # Getter
    def get_isbn(self):
        return self.isbn

    # Setter
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn