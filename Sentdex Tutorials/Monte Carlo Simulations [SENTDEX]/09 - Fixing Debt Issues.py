import random
import time
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

sampleSize = 1000
startingFunds = 10000
wagerSize = 100
wagerCount = 10000


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


def double_bettor(funds, initial_wager, wager_count, color):
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
    color : str
        The color with wich the returned value with be plotted

    Returns
    value : int
        The sum of 100 random wagers
    =======

    '''
    value = funds
    wager = initial_wager
    global broke_count
    wX = []
    vY = []

    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if roll_dice():
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    broke_count += 1
                    break

        elif previousWager == 'loss':
            if roll_dice():
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2

                if (value - wager) < 0:
                    wager = value

                value -= wager
                previousWagerAmount = wager

                wX.append(currentWager)
                vY.append(value)

                if value <= 0:
                    broke_count += 1
                    break

                previousWager = 'loss'

                if value < 0:
                    broke_count += 1
                    break

        currentWager += 1
    # print(value)

    plt.plot(wX, vY, color)


def simple_bettor(funds, initial_wager, wager_count, color):
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
    color : str
        The color with wich the returned value with be plotted

    Returns
    value : int
        The sum of 100 random wagers
    =======

    '''
    global broke_count
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

    if value <= 0:
        value = 'broke'
    # print('Funds: {}'.format(value))

    plt.plot(wX, vY, color)


xx = 0
broke_count = 0
while xx < sampleSize:
    simple_bettor(startingFunds, wagerSize, wagerCount, 'k')
    double_bettor(startingFunds, wagerSize, wagerCount, 'c')
    xx += 1

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.axhline(0, color='r')
plt.show()
