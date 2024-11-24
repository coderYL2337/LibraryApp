# test_library.py (with user management tests)

import unittest
from datetime import datetime, timedelta
from library_system import Book, Library, User

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227")
        self.user = User("U001", "John Doe")
        self.library.add_book(self.book)
        self.library.add_user(self.user)

    def test_user_borrow_return(self):
        self.assertTrue(self.library.borrow_book("978-0547928227", "U001"))
        user_books = self.library.get_user_books("U001")
        self.assertEqual(len(user_books), 1)
        self.assertEqual(user_books[0].title, "The Hobbit")
        
        self.assertTrue(self.library.return_book("978-0547928227"))
        self.assertEqual(len(self.library.get_user_books("U001")), 0)

    def test_overdue_books(self):
        self.library.borrow_book("978-0547928227", "U001")
        self.book.borrow_date = datetime.now() - timedelta(days=15)
        overdue = self.library.get_overdue_books()
        self.assertEqual(len(overdue), 1)
        self.assertEqual(overdue[0].isbn, "978-0547928227")

if __name__ == '__main__':
    unittest.main()