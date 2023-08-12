#!/usr/bin/python3
import builtins

def print_names(module):
    names = [name for name in dir(module) if not name.startswith('__')]
    names.sort()  # Sort names alphabetically
    for name in names:
        print(name)

        if __name__ == "__main__":
            try:
                import hidden_4  # Import the module
                print_names(hidden_4)  # Print the names
            except ImportError:
                print("Module 'hidden_4' not found.")
