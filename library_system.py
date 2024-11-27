# library_system.py (updated with user management)

from typing import Dict, List, Optional
from datetime import datetime, timedelta
from library_stats import LibraryStatistics  # Add this import

class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.borrowed_books: Dict[str, datetime] = {}  # isbn -> borrow_date
        self.stats = LibraryStatistics(self)  # Add this line

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by: Optional[str] = None
        self.borrow_date: Optional[datetime] = None

class Library:
    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.users: Dict[str, User] = {}
        self.max_borrow_days = 14

    def add_book(self, book: Book):
        self.books[book.isbn] = book

    def add_user(self, user: User):
        self.users[user.user_id] = user

    def find_book(self, isbn: str) -> Optional[Book]:
        return self.books.get(isbn)

    def find_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def borrow_book(self, isbn: str, user_id: str) -> bool:
        book = self.find_book(isbn)
        user = self.find_user(user_id)
        
        if not (book and user):
            return False
            
        if book.is_borrowed:
            return False
            
        book.is_borrowed = True
        book.borrowed_by = user_id
        book.borrow_date = datetime.now()
        user.borrowed_books[isbn] = book.borrow_date
        return True

    def return_book(self, isbn: str) -> bool:
        book = self.find_book(isbn)
        if not book or not book.is_borrowed:
            return False

        user = self.find_user(book.borrowed_by)
        if user:
            del user.borrowed_books[isbn]

        book.is_borrowed = False
        book.borrowed_by = None
        book.borrow_date = None
        return True

    def get_overdue_books(self) -> List[Book]:
        overdue = []
        current_time = datetime.now()
        for book in self.books.values():
            if (book.is_borrowed and book.borrow_date and 
                current_time - book.borrow_date > timedelta(days=self.max_borrow_days)):
                overdue.append(book)
        return overdue

    def get_user_books(self, user_id: str) -> List[Book]:
        user = self.find_user(user_id)
        if not user:
            return []
        return [self.books[isbn] for isbn in user.borrowed_books]
    
    def get_statistics_report(self) -> str:
        return self.stats.generate_report()

# Example usage
if __name__ == "__main__":
    library = Library()
    
    # Add books
    book1 = Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    library.add_book(book1)
    library.add_book(book2)
    
    # Add user
    user = User("U001", "John Doe")
    library.add_user(user)
    
    # Borrow books
    library.borrow_book("978-0547928227", "U001")
    print(library.get_user_books("U001"))  # [book1]