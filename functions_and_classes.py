#!/usr/bin/env python3
"""
Functions and Classes Example - Python 2026 Tutorial
====================================================
This example demonstrates:
- Function definitions and usage
- Classes and objects
- Object-oriented programming basics
"""

def greet(name, greeting="Hello"):
    """
    A simple function that greets a person.
    
    Args:
        name (str): The name of the person to greet
        greeting (str): The greeting to use (default: "Hello")
    
    Returns:
        str: The formatted greeting message
    """
    return f"{greeting}, {name}!"

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    return length * width

class Book:
    """A class representing a book."""
    
    def __init__(self, title, author, year):
        """
        Initialize a new Book.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"'{self.title}' by {self.author} ({self.year})"
    
    def is_classic(self):
        """
        Determine if the book is a classic (more than 50 years old).
        
        Returns:
            bool: True if the book is more than 50 years old
        """
        return 2026 - self.year > 50

class Library:
    """A class representing a library that contains books."""
    
    def __init__(self, name):
        """
        Initialize a new Library.
        
        Args:
            name (str): The name of the library
        """
        self.name = name
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book (Book): The book to add
        """
        self.books.append(book)
        print(f"Added {book} to {self.name}")
    
    def list_books(self):
        """List all books in the library."""
        print(f"\nBooks in {self.name}:")
        if not self.books:
            print("  No books yet!")
        else:
            for i, book in enumerate(self.books, 1):
                classic = " (Classic!)" if book.is_classic() else ""
                print(f"  {i}. {book}{classic}")

def main():
    """Run demonstrations of functions and classes."""
    print("Python Functions and Classes Tutorial - 2026\n")
    
    # Function examples
    print("=== Functions ===")
    print(greet("Alice"))
    print(greet("Bob", "Hi"))
    area = calculate_area(5, 3)
    print(f"Area of 5x3 rectangle: {area}")
    print()
    
    # Class examples
    print("=== Classes and Objects ===")
    book1 = Book("Python Programming", "John Doe", 2026)
    book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book3 = Book("1984", "George Orwell", 1949)
    
    library = Library("Central Library")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    library.list_books()
    print("\nTutorial complete!")

if __name__ == "__main__":
    main()
