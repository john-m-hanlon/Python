import random


def roll_dice(x):
    '''
    Takes an argument x and returns a random integer

    Parameters
    ==========
    x : int
        Random positive integer

    Returns
    =======
    roll : int
        returns a random between 1 and the provided argument
    '''
    i = 0
    while i < x:
        roll = random.randint(1, x)
        print(roll)
        i += 1


roll_dice(100)
