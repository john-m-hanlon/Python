""" This file contains code for use with "Intermediate Python Programming" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

import timeit

input_list = range(100)


def div_by_five(num):
    '''
    Takes an argument, any number, and checks to see if it is divisible by 5

    Parameters
    ==========
    num : int
        Any integer number

    Returns
    =======
    True : Command
        The number is divisible by 5

    False: Command
        The number is not divislbe by 5
    '''

    # if the remainder of the number is 0, it is divisible by 5, return True
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))
xyz = [(i for i in input_list if div_by_five(i))]

print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = list(i for i in input_list if div_by_five(i))''', number=5000))
