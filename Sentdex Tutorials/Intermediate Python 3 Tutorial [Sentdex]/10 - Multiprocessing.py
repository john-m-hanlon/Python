""" This file contains code for use with "Intermediate Python Programming" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

import multiprocessing


def spawn(num, num2):
    '''
    Prints the string 'Spawned!' as will as the iteration range

    Parameters
    ==========
    num : int
        the first iteration count

    num2 : int
        the second iteration count
        
    Returns
    =======
    x : str
        Returns the string incased in the variable x
    '''

    x = 'Spawned! {} {}'.format(num, num2)
    print(x)
    return x


if __name__ == '__main__':
    for i in range(500):
        p = multiprocessing.Process(target=spawn, args=(i, i + 1))
        p.start()
        p.join()
