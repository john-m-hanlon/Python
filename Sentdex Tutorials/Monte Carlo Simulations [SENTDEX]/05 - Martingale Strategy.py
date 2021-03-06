import random
import time
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


def roll_dice():
    '''
    Takes no arguments

    Parameters
    ==========

    Returns
    =======
    roll : int
        returns True only if value between 51-99
    '''
    roll = random.randint(1, 100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll > 50:
        return True


def double_bettor(funds, initial_wager, wager_count):
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

    wX = []
    vY = []

    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            print('we won the last wager, great')
            if roll_dice():
                value += wager
                print(value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                print(value)
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    print('we went broke after {} bets'.format(currentWager))
                    break

        elif previousWager == 'loss':
            print('We lost the last one, so we will double down!!!')
            if roll_dice():
                wager = previousWagerAmount * 2
                print('We won {}'.format(wager))
                value += wager
                print(value)
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                print('We lost {}'.format(wager))
                value -= wager
                if value < 0:
                    print('We went broke after {} bets'.format(currentWager))

                print(value)
                previousWager = 'loss'
                previousWagerAmount = wager

                wX.append(currentWager)
                vY.append(value)

                if value < 0:
                    print('We went broke after {} bets'.format(currentWager))
                    break

        currentWager += 1
    print(value)

    plt.plot(wX, vY)


double_bettor(10000, 100, 1000)
plt.show()


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

    wX = []
    vY = []

    currentWager = 1

    while currentWager <= wager_count:
        if roll_dice():
            value += wager
            wX.append(currentWager)
            vY.append(value)

        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

        currentWager += 1

    if value < 0:
        value = 'broke'
    # print('Funds: {}'.format(value))

    plt.plot(wX, vY)


# x = 0
# while x < 1000:
#     simple_bettor(10000, 100, 100000)
#     x += 1

# plt.ylabel('Account Value')
# plt.xlabel('Wager Count')
# plt.show()
