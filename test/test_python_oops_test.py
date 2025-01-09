import unittest
from other_practice.python_oops_test import *

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        # Setup for each test
        self.library = Library()
        self.librarian = Librarian("Alice")

        # Books
        self.book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "111")
        self.book2 = Book("1984", "George Orwell", "222")

        # Members
        self.member = Member("John Doe", "M001")
        self.library.register_member(self.member)

        # Librarian adds books to the library
        self.librarian.add_book(self.library, self.book1)
        self.librarian.add_book(self.library, self.book2)

    def test_add_and_remove_book(self):
        # Test adding a book
        self.assertIn(self.book1, self.library.books)
        self.assertIn(self.book2, self.library.books)







