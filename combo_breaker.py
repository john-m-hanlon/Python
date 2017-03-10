""" This file contains code for use with "Intermediate Python Programming" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

from string import ascii_lowercase
import getpass
# for c in ascii_lowercase:
#     print(c)

# correct_combo1 = int(input('This is the raw input 1: '))
# correct_combo2 = int(input('This is the raw input 2: '))
# correct_combo3 = int(input('This is the raw input 3: '))

# cc1, cc2, cc3 = int(input('Here:')), int(input()), int(input())

start = getpass.getpass("P/w: ")

x = ascii_lowercase

if 'a' in x:
    print('Okay')



# correct_combo = (correct_combo1, correct_combo2, correct_combo3)
# correct_combo = (cc1, cc2, cc3)
correct_combo = (int(start[0]), int(start[1]), int(start[2]))

def combo_gen():
    '''
    Yields thing in a stream

    Parameters
    ==========
    Takes no parameters

    Returns
    =======
    Returns nothing

    '''
    for c1 in range(10) or ascii_lowercase:
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)


for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == correct_combo:
        print('Found the combo: {}-{}-{}'.format(c1, c2, c3))
        break
    print(c1, c2, c3)
