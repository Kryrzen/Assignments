# Author: Vinoshan
# College Email: vino.kugendran@students.williscollege.com
# File Name: capitalize_last_name.py
# Description: Accepts a string with a first and last name, and returns a string in which only the
#              first letter of the first name is uppercase and all letters of the last name are uppercase.


def capitalize_last_name(full_name):
    # Validate input type
    if not isinstance(full_name, str):
        raise TypeError("Input must be a string.")

    # Split the input into parts and strip any extra whitespace
    parts = full_name.strip().split()

    # Validate structure
    if len(parts) != 2:
        raise ValueError("Input must contain exactly two words: first and last name.")

    first, last = parts

    # Validate characters making sure it contains only alphabetic letters
    if not first.isalpha() or not last.isalpha():
        raise ValueError("Names must contain only alphabetic letters (A–Z).")

    # Capitalize correctly
    first = first.capitalize()
    last = last.upper()

    return f"{first} {last}"


def main():
    try:
        # Get user input
        name = input("Enter a first and last name: ")
        # Process the name and print the result
        result = capitalize_last_name(name)
        print("Formatted name:", result)

    except (TypeError, ValueError) as e:
        # Print the error message if an exception occurs
        print("Error:", e)


# Run the program
main()
