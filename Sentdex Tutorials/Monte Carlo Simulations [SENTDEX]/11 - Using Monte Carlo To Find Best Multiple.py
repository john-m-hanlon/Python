import random
import time
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

lower_bust = 31.235
higher_profit = 63.208

sampleSize = 100
startingFunds = 10000
wagerSize = 100
wagerCount = 100


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


def multiple_bettor(funds, initial_wager, wager_count):
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

    global multiple_busts
    global multiple_profits

    value = funds
    wager = initial_wager
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
                    multiple_busts += 1
                    break

        elif previousWager == 'loss':
            if roll_dice():
                wager = previousWagerAmount * random_multiple
                if (value - wager) < 0:
                    wager = value
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * random_multiple

                if (value - wager) <= 0:
                    wager = value

                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

                if value <= 0:
                    multiple_busts += 1
                    break

        currentWager += 1

    if value > funds:
        multiple_profits += 1


def doubler_bettor(funds, initial_wager, wager_count, color):
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
    global doubler_busts
    global doubler_profits
    value = funds
    wager = initial_wager

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
                if value < 0:
                    currentWager += 1000000000000
                    doubler_busts += 1

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
                    currentWager += 1000000000000
                    doubler_busts += 1

                previousWager = 'loss'

        currentWager += 1
    # print(value)

    plt.plot(wX, vY, color)
    if value > funds:
        doubler_profits += 1


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
    global simple_busts
    global simple_profits
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

            if value <= 0:
                currentWager += 100000000000000
                simple_busts += 1

        currentWager += 1

    plt.plot(wX, vY, color)
    if value > funds:
        simple_profits += 1


while True:
    multiple_busts = 0.0
    multiple_profits = 0.0

    multiple_samp_size = 1000
    currentSample = 1

    random_multiple = random.uniform(0.1, 10.0)

    while currentSample <= multiple_samp_size:
        multiple_bettor(startingFunds, wagerSize, wagerCount)
        currentSample += 1

    if ((multiple_busts / multiple_samp_size) * 100.00 < lower_bust) \
            and ((multiple_busts / multiple_samp_size) * 100.00 >
                 higher_profit):

        print('#' * 50)
        print('Found a winner, the multiple was: {}'.format(random_multiple))
        print('Lower bust to beat: {}'.format(lower_bust))
        print('Higher profit rate to beat: {}'.format(higher_profit))
        print('Bust rate: {}'.format((multiple_busts / multiple_samp_size) *
              100.00))
        print('Profit Rate: {}'.format((multiple_profits /
                                       multiple_samp_size) * 100.00))
        print('#' * 50)
'''
    else:
        print('#' * 50)
        print('Found a loser, the multiple was: {}'.format(random_multiple))
        print('Lower bust to beat: {}'.format(lower_bust))
        print('Higher profit rate to beat: {}'.format(higher_profit))
        print('Bust rate: {}'.format((multiple_busts / multiple_samp_size) *
              100.00))
        print('Profit Rate: {}'.format((multiple_profits /
                                       multiple_samp_size) * 100.00))
        print('#' * 50)
'''
