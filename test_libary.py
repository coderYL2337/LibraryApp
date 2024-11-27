# test_library.py (with user management tests)

import unittest
from datetime import datetime, timedelta
from library_system import Book, Library, User
from library_stats import LibraryStatistics

class TestLibraryStats(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        
        # Add books
        self.books = [
            Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227"),
            Book("1984", "George Orwell", "978-0451524935"),
            Book("Pride and Prejudice", "Jane Austen", "978-0141439518")
        ]
        for book in self.books:
            self.library.add_book(book)
        
        # Add users
        self.users = [
            User("U001", "John Doe"),
            User("U002", "Jane Smith")
        ]
        for user in self.users:
            self.library.add_user(user)

    def test_borrow_tracking(self):
        # Simulate some borrows
        self.library.borrow_book("978-0547928227", "U001")
        self.library.borrow_book("978-0451524935", "U001")
        self.library.borrow_book("978-0547928227", "U002")
        
        # Test most popular books
        popular_books = self.library.stats.get_most_popular_books()
        self.assertEqual(popular_books[0][0], "978-0547928227")
        self.assertEqual(popular_books[0][1], 2)  # borrowed twice

    def test_active_users(self):
        # Simulate some borrows
        self.library.borrow_book("978-0547928227", "U001")
        self.library.borrow_book("978-0451524935", "U001")
        self.library.borrow_book("978-0141439518", "U002")
        
        active_users = self.library.stats.get_active_users()
        self.assertEqual(active_users[0][0], "U001")
        self.assertEqual(active_users[0][1], 2)  # borrowed twice

    def test_monthly_stats(self):
        # Simulate some borrows
        self.library.borrow_book("978-0547928227", "U001")
        self.library.borrow_book("978-0451524935", "U002")
        
        monthly_stats = self.library.stats.get_monthly_borrows()
        current_month = datetime.now().strftime("%Y-%m")
        self.assertEqual(monthly_stats[current_month], 2)

    def test_report_generation(self):
        # Simulate some activity
        self.library.borrow_book("978-0547928227", "U001")
        self.library.borrow_book("978-0451524935", "U002")
        
        report = self.library.stats.generate_report()
        self.assertIn("Library Statistics Report", report)
        self.assertIn("Most Popular Books:", report)
        self.assertIn("Most Active Users:", report)
        self.assertIn("Monthly Statistics:", report)

if __name__ == '__main__':
    unittest.main()