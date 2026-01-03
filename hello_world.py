#!/usr/bin/env python3
"""
Hello World Example - Python 2026 Tutorial
===========================================
This is the classic first program in any programming language.
It demonstrates basic Python syntax and how to print output.
"""

def main():
    """Main function that prints a greeting."""
    # Simple print statement
    print("Hello, World!")
    
    # Print with variables
    year = 2026
    message = f"Welcome to Python programming in {year}!"
    print(message)
    
    # Multiple greetings
    greetings = ["Hello", "Hi", "Hey", "Greetings"]
    for greeting in greetings:
        print(f"{greeting}, Python learner!")

if __name__ == "__main__":
    main()
