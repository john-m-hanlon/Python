""" This file contains code for use with "Intermediate Python Programming" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

import argparse
import sys


def main():
    """

    Parameters
    ==========

    Returns
    =======

    """

    parser = argparse.ArgumentParser()

    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? (add, sub, mul, or div)')

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


def calc(args):
    """ Algebraic calculation of two variables. Analytic formula.

    Parameters
    ==========
    args : statement
        Arguments from the main() function

    Returns
    =======
    value : float
        Output of variables and algebraic operation
    """

    if args.operation == 'add':
        value = args.x + args.y
        return value

    elif args.operation == 'sub':
        value = args.x - args.y
        return value

    elif args.operation == 'mul':
        value = args.x * args.y
        return value

    elif args.operation == 'div':
        value = args.x / args.y
        return value


if __name__ == '__main__':
    main()
