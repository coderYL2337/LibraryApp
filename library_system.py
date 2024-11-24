class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = {}  # isbn -> Book

    def add_book(self, book: Book):
        self.books[book.isbn] = book

    def find_book(self, isbn: str) -> Book:
        return self.books.get(isbn)

    def borrow_book(self, isbn: str) -> bool:
        book = self.find_book(isbn)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            return True
        return False

    def return_book(self, isbn: str) -> bool:
        book = self.find_book(isbn)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return True
        return False

# Example usage
if __name__ == "__main__":
    library = Library()
    book = Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227")
    library.add_book(book)
    print(library.borrow_book("978-0547928227"))  # True
    print(library.borrow_book("978-0547928227"))  # False