#!/usr/bin/env python3
"""
Q Dev App - Simple Demo Application
"""

def main():
    """Main application function"""
    print("Welcome to Q Dev App!")
    print("This is a simple demo application for testing purposes.")
    print("You can extend this application with your own code.")
    
    # Example functionality
    name = input("What's your name? ")
    print(f"Hello, {name}! Thanks for trying Q Dev App.")
    
    # Return success
    return 0

if __name__ == "__main__":
    exit(main())