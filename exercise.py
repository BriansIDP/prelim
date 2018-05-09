#!/usr/bin/env python3
"""Preliminary exercises for Part IIA Project GF2."""
import sys

from mynames import MyNames


def open_file(path):
    """Open and return the file specified by path."""
    try:
        f = open(path, 'r+')
        return f
    except FileNotFoundError:
        print("Path not correct!")
        sys.exit()


def get_next_character(input_file):
    """Read and return the next character in input_file."""
    character = input_file.read(1)
    return character


def get_next_non_whitespace_character(input_file):
    """Seek and return the next non-whitespace character in input_file."""
    character = input_file.read(1)
    while character.isspace():
        character = input_file.read(1)
    return character


def get_next_number(input_file):
    """Seek the next number in input_file.

    Return the number (or None) and the next non-numeric character.
    """
    number = ''
    character = input_file.read(1)
    while not character.isdigit():
        character = input_file.read(1)
        if character == '':
            return [None, '']
    while character.isdigit():
        number += character
        character = input_file.read(1)
    if number == '':
        number = None
    else:
        number = int(number)
    return [number, character]


def get_next_name(input_file):
    """Seek the next name string in input_file.

    Return the name string (or None) and the next non-alphanumeric character.
    """
    name = ''
    character = input_file.read(1)
    while not character.isalpha():
        character = input_file.read(1)
        if character == '':
            return [None, '']
    while character.isalnum():
        name += character
        character = input_file.read(1)
    if name == '':
        name = None
    return [name, character]


def main():
    """Preliminary exercises for Part IIA Project GF2."""

    # Check command line arguments
    arguments = sys.argv[1:]
    if len(arguments) != 1:
        print("Error! One command line argument is required.")
        sys.exit()

    else:
        # Print the path provided and try to open the file for reading
        print('Openning: '+arguments[0])
        f = open_file(arguments[0])

        print("\nNow reading file...")
        n = " "
        while n != '':
            n = get_next_character(f)
            print(n, end="")
        # Print out all the characters in the file, until the end of file

        print("\nNow skipping spaces...")
        # Print out all the characters in the file, without spaces
        # Reset pointer
        f.seek(0)

        n = " "
        while n != '':
            n = get_next_non_whitespace_character(f)
            print(n, end="")

        print("\nNow reading numbers...")
        # Print out all the numbers in the file
        print('\n')
        f.seek(0)

        n = " "
        while n != '':
            number, n = get_next_number(f)
            print(number, end="")

        print("\nNow reading names...")
        # Print out all the names in the file

        f.seek(0)

        n = " "
        while n != '':
            name, n = get_next_name(f)
            print(name)
        print('\n')

        print("\nNow censoring bad names...")
        # Print out only the good names in the file
        f.seek(0)
        name = MyNames()

        bad_name_ids = [name.lookup("Terrible"), name.lookup("Horrid"),
                        name.lookup("Ghastly"), name.lookup("Awful")]
        n = " "
        while n != '':
            next_name, n = get_next_name(f)
            if next_name is not None:
                ID = name.lookup(next_name)
                if ID is not None and ID not in bad_name_ids:
                    print(name.get_string(ID))


if __name__ == "__main__":
    main()
