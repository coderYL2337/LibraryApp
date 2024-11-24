# Add this new file: library_stats.py
from datetime import datetime
from typing import Dict, List, Tuple
from collections import Counter

class LibraryStatistics:
    def __init__(self, library):
        self.library = library
        self.borrow_history: List[Tuple[str, str, datetime]] = []  # [(isbn, user_id, date)]

    def record_borrow(self, isbn: str, user_id: str):
        self.borrow_history.append((isbn, user_id, datetime.now()))

    def get_most_popular_books(self, limit: int = 5) -> List[Tuple[str, int]]:
        book_borrows = Counter(isbn for isbn, _, _ in self.borrow_history)
        return book_borrows.most_common(limit)

    def get_active_users(self, limit: int = 5) -> List[Tuple[str, int]]:
        user_borrows = Counter(user_id for _, user_id, _ in self.borrow_history)
        return user_borrows.most_common(limit)

    def get_monthly_borrows(self) -> Dict[str, int]:
        monthly_stats = {}
        for _, _, date in self.borrow_history:
            month_key = date.strftime("%Y-%m")
            monthly_stats[month_key] = monthly_stats.get(month_key, 0) + 1
        return monthly_stats

    def generate_report(self) -> str:
        report = []
        report.append("=== Library Statistics Report ===\n")
        
        # Popular books
        report.append("Most Popular Books:")
        for isbn, count in self.get_most_popular_books():
            book = self.library.find_book(isbn)
            if book:
                report.append(f"- {book.title}: {count} borrows")
        
        # Active users
        report.append("\nMost Active Users:")
        for user_id, count in self.get_active_users():
            user = self.library.find_user(user_id)
            if user:
                report.append(f"- {user.name}: {count} borrows")
        
        # Monthly stats
        report.append("\nMonthly Statistics:")
        for month, count in sorted(self.get_monthly_borrows().items()):
            report.append(f"- {month}: {count} borrows")
            
        return "\n".join(report)