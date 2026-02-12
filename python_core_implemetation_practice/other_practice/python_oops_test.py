# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, isbn={self.isbn}, available={self.is_available})>"

# Member Class
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            return True
        return False

    def __repr__(self):
        return f"<Member(name={self.name}, member_id={self.member_id}, borrowed_books={len(self.borrowed_books)})>"

# Librarian Class
class Librarian:
    def __init__(self, name):
        self.name = name

    def add_book(self, library, book):
        library.books.append(book)

    def remove_book(self, library, book):
        if book in library.books and book.is_available:
            library.books.remove(book)
            return True
        return False

    def __repr__(self):
        return f"<Librarian(name={self.name})>"

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def register_member(self, member):
        self.members.append(member)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def is_book_available(self, isbn):
        book = self.find_book(isbn)
        return book.is_available if book else False

    def __repr__(self):
        return f"<Library(total_books={len(self.books)}, total_members={len(self.members)})>"
