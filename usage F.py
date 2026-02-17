def main():
    library = []

    # Create books
    book1 = Book("Python Basics", "Potter", "12345")
    book2 = Book("OOP in Python", "Malfoy", "67890")

    # Staff member
    staff = StaffMember("Ali", "M001", "S100")
    staff.add_book(library, book1)
    staff.add_book(library, book2)

    # Member
    member = Member("Ahmed", "M002")
    member.borrow_book(book1)

    print("\nBook Info:")
    book1.display_info()

    member.return_book(book1)


if __name__ == "main":
    main()