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
        if roll == 100:
            # print('{} roll was 100, you lose! What are the odds!'.format(roll))
            return False

        elif roll <= 50:
            # print('{} roll was less than 50, you lose!'.format(roll))
            return False

        elif 100 > roll > 50:
            # print('{} roll was greater than 50, you WIN!'.format(roll))
            return True

        print(roll)
        i += 1


roll_dice(100)


def simple_bettor(funds, initial_wager, wager_count):
    '''
    Takes three arguments and returns

    Parameters
    ==========
    funds : int
        How much money the user started with
    initial_wager : int
        How much user bets each time
    wager_count : int
        How many times the user particpates in the exercise

    Returns
    value : int
        The sum of 100 random wagers
    =======

    '''
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager < wager_count:
        if roll_dice(wager_count):
            value += wager
        else:
            value -= wager

        currentWager += 1
        
    if value < 0:
        value = 'broke'
    print('Funds: {}'.format(value))


x = 0
while x < 100:
    simple_bettor(10000, 100, 1000)
    x += 1
