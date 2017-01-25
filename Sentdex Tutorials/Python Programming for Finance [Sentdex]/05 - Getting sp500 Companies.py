""" This file contains code for use with "Python Programming for Finance" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

import bs4 as bs
import pickle
import requests

floc = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Python ' \
       'Programming for Finance [Sentdex]/Data Examples/'


def save_sp500_tickers():
    '''
    Takes no arguments; returns a list of all tickers in the S&P500 indx

    Parameters
    ==========

    Returns
    =======
    tickers : list
        returns list of companies in the S&P 500 index
    '''
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_'
                        '500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(tickers)

    with open('{}sp500tickers.pickle'.format(floc), 'wb') as f:
        pickle.dump(ticker, f)

    print(tickers)

    return tickers


save_sp500_tickers()
