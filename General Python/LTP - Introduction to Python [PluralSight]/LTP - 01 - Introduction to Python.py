#
# Simple script which takes input from a user and assigns it to be their
# favorite number!
# LTP -01 - Introduction to Python.py
#

__author__ = 'JohnHanlon'

# What is your favorite number?


def favorite_number():
    ''' Asks for your favorite number and returns the same

    Parameters
    ==========
    N/A : takes no parameters

    Returns
    =======
    value : str
        Sentence with your favorite number
    '''
    print('Hello, what is your favorite number?')
    number = input()
    value = 'Your favorite number is {}'.format(number)
    return value


# print(favorite_number())


def random_number_guesser():
    ''' Asks for a number and gives the user several attempts to guess the
    number

    Parameters
    ==========
    N/A : takes no parameters

    Returns
    =======
    magic_number : int
        random magic number
    '''

    import random

    min_number = 1
    max_number = 100
    magic_number = random.randint(min_number, max_number)

    message = 'The magic number is between {0} and {1}'.format(min_number,
                                                               max_number)
    print(message)
    found = False

    while not found:
        print('Hello, what is the magic number?')
        usr_input = int(input())

        if usr_input == magic_number:
            found = True

        elif usr_input < magic_number:
            print('Your guess is too low')

        elif usr_input > magic_number:
            print('Your guess is too high')

    print('You got it')


random_number_guesser()
