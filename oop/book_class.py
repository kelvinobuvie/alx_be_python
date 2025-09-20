# alx_be_python/oop/book_class.py

class Book:
    """A class representing a book with magic methods."""

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Human-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation for recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Called when the object is deleted."""
        print(f"Deleting {self.title}")
