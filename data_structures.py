#!/usr/bin/env python3
"""
Data Structures Example - Python 2026 Tutorial
===============================================
This example demonstrates the most common Python data structures:
- Lists
- Tuples
- Dictionaries
- Sets
"""

def demonstrate_lists():
    """Show how to work with lists."""
    print("=== Lists ===")
    # Create a list
    fruits = ["apple", "banana", "cherry", "date"]
    print(f"Fruits: {fruits}")
    
    # Add an item
    fruits.append("elderberry")
    print(f"After append: {fruits}")
    
    # Access by index
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    
    # List slicing
    print(f"First three: {fruits[:3]}")
    print()

def demonstrate_tuples():
    """Show how to work with tuples."""
    print("=== Tuples ===")
    # Tuples are immutable
    coordinates = (10, 20, 30)
    print(f"Coordinates: {coordinates}")
    print(f"X: {coordinates[0]}, Y: {coordinates[1]}, Z: {coordinates[2]}")
    print()

def demonstrate_dictionaries():
    """Show how to work with dictionaries."""
    print("=== Dictionaries ===")
    # Create a dictionary
    student = {
        "name": "Alice",
        "age": 20,
        "major": "Computer Science",
        "year": 2026
    }
    print(f"Student: {student}")
    
    # Access values
    print(f"Name: {student['name']}")
    print(f"Major: {student['major']}")
    
    # Add new key-value pair
    student["gpa"] = 3.8
    print(f"Updated student: {student}")
    print()

def demonstrate_sets():
    """Show how to work with sets."""
    print("=== Sets ===")
    # Sets contain unique elements
    numbers = {1, 2, 3, 4, 5}
    print(f"Numbers: {numbers}")
    
    # Add duplicate (won't be added)
    numbers.add(3)
    print(f"After adding 3 again: {numbers}")
    
    # Set operations
    evens = {2, 4, 6, 8}
    print(f"Evens: {evens}")
    print(f"Union: {numbers.union(evens)}")
    print(f"Intersection: {numbers.intersection(evens)}")
    print()

def main():
    """Run all demonstrations."""
    print("Python Data Structures Tutorial - 2026\n")
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_dictionaries()
    demonstrate_sets()
    print("Tutorial complete!")

if __name__ == "__main__":
    main()
