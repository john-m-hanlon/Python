""" This file contains code for use with "Intermediate Python Programming" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

def simple_gen():
    '''
    A simple generator that allows us to iterate over the yielded components

    Parameters
    ==========
    Takes no parameters

    Returns
    =======
    Returns nothing
    '''

    yield 'Oh'
    yield 'hello'
    yield 'there'


for i in simple_gen():
    print(i)

correct_combo = (3, 6, 1)
found_combo = False

for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == correct_combo:
                print('Found the combo: {}'.format((c1, c2, c3)))
                found_combo = True
                break
            print(c1, c2, c3)


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
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == correct_combo:
        print('Found the combo: {}'.format((c1, c2, c3)))
        break
    print(c1, c2, c3)

