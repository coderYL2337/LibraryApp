import unittest
from library_system import Book, Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227")
        self.library.add_book(self.book)

    def test_add_find_book(self):
        found_book = self.library.find_book("978-0547928227")
        self.assertEqual(found_book.title, "The Hobbit")
        self.assertEqual(found_book.author, "J.R.R. Tolkien")

    def test_borrow_return_book(self):
        self.assertTrue(self.library.borrow_book("978-0547928227"))
        self.assertFalse(self.library.borrow_book("978-0547928227"))
        self.assertTrue(self.library.return_book("978-0547928227"))

if __name__ == '__main__':
    unittest.main()