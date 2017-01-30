""" This file contains code for use with "Intermediate Python Programming" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

from multiprocessing import Pool


def job(num):
    '''
    Each multiprocessed job number

    Paramters
    =========
    num : int
        The amount of processings in the multithread job

    Returns
    =======
    x : int
        The final amount of processings in the multithread job    
    '''

    x = num * 2
    return x


if __name__ == '__main__':
    p = Pool(processes=20)
    data = p.map(job, range(20))
    data2 = p.map(job, [5, 2])
    p.close()
    print(data)
    print(data2)
