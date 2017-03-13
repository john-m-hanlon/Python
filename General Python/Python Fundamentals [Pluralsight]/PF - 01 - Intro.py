#
# A simple program to count the words in a given text
# PF - 01 - Intro.py
#

__author__ = 'JohnHanlon'

import sys


def count_words(filename):
    ''' Counts the number of words in a give text

    Parameters
    ==========
    filename : file
        the while which will be analyzed

    Returns
    =======
    N/A : returns nothing
    '''

    results = dict()
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                results[word] = results.setdefault(word, 0) + 1

    for word, count in sorted(results.items(), key=lambda x: x[1]):
        print('{} {}'.format(count, word))


# count_words(sys.argv[1])

count_words('test_file.txt')
