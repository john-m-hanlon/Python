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
    rand_word : str
        random word
    '''

    rand_word = 'pizza'
    return rand_word


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

    while playing:
        strikes += 1

        if strikes >= max_strikes:
            playing = False

    if strikes >= max_strikes:
        print('Loser')
    else:
        print('Winner')




print('Game started')
play_word_game()
print('Game over')