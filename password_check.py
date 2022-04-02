"""
Description: A simple password checker

Name: Nurul Syafini Subhan
"""


def is_valid_password(text):
    """Check whether a given text has the correct password format"""
    return 8 <= len(text) <= 20


def main():
    """Start program"""
    get_password()


def get_password():
    new_password = input("Input password: ")
    print_asterisk(new_password)


def print_asterisk(new_password):
    new_password = len(new_password)
    for i in range(new_password):
        print('*', end='')


main()
