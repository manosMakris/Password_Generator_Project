import random
import string
import os

def remove_chars(string: str, chars_to_remove) -> str:
    '''
    Description: 
    Removes the characters in the iterable chars_to_remove from the string.

    Arguments:
    string: The string from which the specified characters will be removed.
    chars_to_remove: The iterable which contains the characters to be removed from the specified string.

    Returns:
    The new string after the deletion operation
    '''
    s = "".join(c for c in string if c not in list("".join(chars_to_remove)))
    return s

def generate_password(min_length: int, numbers=False, special=False, unique=True, save=True) -> str:
    '''
    Description:
    Generates a password which fullfils the arguments specifications.

    Arguments:
    min_length: The minimum length of the password.
    numbers: If any numbers should be included.
    special: If any special characters should be included.
    unique: If any duplicates are allowed or not.
    save: If the password should be saved to a password.txt file.

    Returns:
    The generated password as a string.
    '''
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special:
        characters += special_characters

    password = ""
    has_digit = False
    has_special = False
    meets_criteria = False

    while (not meets_criteria) or (len(password) < min_length):
        new_character = random.choice(characters)
        password += new_character
        if unique:
            characters = remove_chars(characters,[new_character])

        if new_character in digits:
            has_digit = True
        if new_character in special_characters:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_digit
        if special:
            meets_criteria = meets_criteria and has_special
    
    if save:
        with open("password.txt", "w") as f:
            f.write(password)
    if not save:
        if os.path.exists("password.txt"):
            os.remove("password.txt")

    return password