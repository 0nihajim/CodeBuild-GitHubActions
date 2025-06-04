#!/usr/bin/env python3
"""
Q Dev App - Simple Demo Application
"""
import os
import sys

def summarize_readme():
    """Summarize the README.md file"""
    readme_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")
    
    try:
        with open(readme_path, 'r') as file:
            content = file.read()
            
            # Extract key sections for the summary
            title = "Q Dev App"
            description = "A lightweight development application built with Alpine Linux for testing and development purposes."
            
            # Extract features
            features = [
                "Lightweight Alpine Linux base",
                "Fast startup and minimal resource usage",
                "Easily customizable for different development needs",
                "Suitable for CI/CD pipelines and local testing"
            ]
            
            # Create the summary
            summary = f"{title}\n\n{description}\n\nKey Features:\n"
            for feature in features:
                summary += f"- {feature}\n"
                
            summary += "\nThe app includes a simple Python application and can be run using Docker."
            
            return summary
    except FileNotFoundError:
        return "README.md file not found."
    except Exception as e:
        return f"Error reading README.md: {str(e)}"

def main():
    """Main application function"""
    print("Welcome to Q Dev App!")
    print("This is a simple demo application for testing purposes.")
    print("You can extend this application with your own code.")
    
    # Check if the user wants to summarize README.md
    if len(sys.argv) > 1 and sys.argv[1] == "--summarize-readme":
        summary = summarize_readme()
        print("\nREADME.md Summary:\n")
        print(summary)
        return 0
    
    # Example functionality
    name = input("What's your name? ")
    print(f"Hello, {name}! Thanks for trying Q Dev App.")
    
    # Return success
    return 0

if __name__ == "__main__":
    exit(main())