""" This file contains code for use with "Python Programming for Finance" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

ploc = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Python ' \
       'Programming for Finance [Sentdex]/Data Examples/'

sloc = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Python ' \
       'Programming for Finance [Sentdex]/'


def save_sp500_tickers():
    '''
    Takes no arguments; returns a list of all tickers in the S&P500 indx

    Parameters
    ==========
    Takes no arguments

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
        tickers.append(ticker)

    with open('{}sp500tickers.pickle'.format(ploc), 'wb') as f:
        pickle.dump(ticker, f)

    print(tickers)

    return tickers


def get_data_from_yahoo(reload_sp500=False):
    '''
    Takes a single, optional argument and pulls the stock prices from
    yahoo.finance given the most recently pickled list of S&P 500 companies
    derived by save_sp500_tickers()

    Parameters
    ==========
    reload_sp500 : argument
        If True, run save_sp500_tickers() to pull a fresh list of the
        companies listed in the S&p 500 according to wikipedia. If False,
        continue pulling data from the saved pickle

    Returns
    {ticker}.csv : csv file
        Returns, and saves, a csv file with the OHLC, Vol, Adj Close data
        for each ticker in the S&P 500
    =======

    '''
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open('{}sp500tickers.pickle'.format(ploc), 'rb') as f:
            tickers = pickle.load(f)

    if not os.path.exists('{}stock_dfs'.format(sloc)):
        os.makedirs('{}stock_dfs'.format(sloc))

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2016, 12, 31)

    for ticker in tickers:
        print(ticker)
        if not os.path.exists('{}stock_dfs/{}.csv'.format(sloc, ticker)):
            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv('{}stock_dfs/{}.csv'.format(sloc, ticker))
        else:
            print('Already have {}'.format(ticker))


get_data_from_yahoo(reload_sp500=True)
