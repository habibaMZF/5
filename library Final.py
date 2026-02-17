# =========================
# Library Management System
# =========================


class Book:
    def init(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn          # private attribute
        self.available = True

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {status}")

    # Getter
    def get_isbn(self):
        return self.isbn

    # Setter
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id   # private attribute
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} borrowed {book.title}")
        else:
            print("Book is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} returned {book.title}")
        else:
            print("This book was not borrowed by this member")

    # Getter
    def get_membership_id(self):
        return self.membership_id


class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, book):
        library.append(book)
        print(f"Book added to library: {book.title}")


def main():
    library = []

    book1 = Book("Python Basics", "Potter", "12345")
    book2 = Book("OOP in Python", "Malfoy", "67890")

    staff = StaffMember("Ali", "M001", "S100")
    staff.add_book(library, book1)
    staff.add_book(library, book2)

    member = Member("Ahmed", "M002")
    member.borrow_book(book1)

    print("\nBook Information:")
    book1.display_info()

    member.return_book(book1)


if name == "main":
    main()