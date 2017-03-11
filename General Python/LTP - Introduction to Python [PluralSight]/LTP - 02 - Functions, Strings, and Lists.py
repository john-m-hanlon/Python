#
# Simple game to find the secret word!!
# LTP - 02 - Functions, Strings, and Lists.py
#

__author__ = 'JohnHanlon'


def get_random_word():
    ''' Pulls in a random word for future analysis

    Parameters
    ==========
    N/A : takes no parameters

    Returns
    =======
    word : str
        random word
    '''
    import random

    words = ['pizza', 'cheese', 'apples']
    word = words[random.randint(0, len(words) - 1)]
    return word


def show_word(word):
    ''' Shows the blanked out word we are trying to guess

    Parameters
    ==========
    word : str
        the word we are trying to guess

    Returns
    =======
    hidden_word : str
        word hidden in underscore and spaces
    '''

    for character in word:
        print('{} '.format(character), end='')
    print('')


def get_guess():
    ''' Guesses a letter in the hidden word

    Parameters
    ==========
    N/A : takes no parameters

    Returns
    =======
    input : str
        user input
    '''

    print('Enter a letter: ')
    return input()


def process_letter(letter, secret_word, blanked_word):
    ''' figures out if the letter is in the secret word

    Parameter
    =========
    letter : str
        the guess entered

    secret_word : str
        the hidden word being evaluated

    blanked_word : str
        converted hidden word

    Return
    ======
    result : binary
        Ture or false if the letter has been found

    '''
    result = False

    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            result = True
            blanked_word[i] = letter

    return result


def print_strikes(number_of_strikes):
    ''' Tests to see if how many strikes have been used

    Parameters
    ==========
    strikes : int
        takes in how many strikes have occured

    Returns
    =======
    remaining : int
        how many strikes are remaining
    '''

    for i in range(0, number_of_strikes):
        print('X', end='')
    print('')


def play_word_game():
    '''

    Parameters
    ==========

    Returns
    =======

    '''
    strikes = 0
    max_strikes = 3
    playing = True

    word = get_random_word()
    blanked_word = list('_' * len(word))

    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, word, blanked_word)

        if not found:
            strikes += 1
            print_strikes(strikes)

        if strikes >= max_strikes:
            playing = False

        if '_' not in blanked_word:
            playing = False

    if strikes >= max_strikes:
        print('Loser!')
    else:
        print('Winner')


print('Game started')
play_word_game()
print('Game over')
