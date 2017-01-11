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


def dAlembert(funds, initial_wager, wager_count):
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

    global da_busts
    global da_profits

    value = funds
    wager = initial_wager
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager

            print('Current wager: {}, value: {}'.format(wager, value))

            if roll_dice():
                value += wager
                print('We won, current value: {}'.format(value))
                previousWagerAmount = wager
            else:
                value -= wager
                previousWager = 'loss'
                print('We lost, current value: {}'.format(value))
                previousWagerAmount = wager

            if value <= 0:
                da_busts += 1
                break

        elif previousWager == 'loss':
            wager = previousWagerAmount + initial_wager
            if (value - wager) <= 0:
                wager = value

            print('Lost the last wager, current wager: {}, value: {}'.
                  format(wager, value))

            if roll_dice():
                value += wager
                print('We won, current value: {}'.format(value))
                previousWagerAmount = wager
                previousWager = 'win'

            else:
                value -= wager
                print('We lost, current value: {}'.format(value))
                previousWagerAmount = wager

                if value <= 0:
                    da_busts += 1
                    break

        currentWager += 1

    if value > funds:
        da_profits += 1


da_busts = 0.0
da_profits = 0.0

dAlembert(startingFunds, wagerSize, wagerCount)
