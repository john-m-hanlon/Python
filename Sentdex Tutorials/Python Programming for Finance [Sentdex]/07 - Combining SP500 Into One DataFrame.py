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

dloc = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Python ' \
       'Programming for Finance [Sentdex]/stock_dfs/'

wiki_link = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'


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
    resp = requests.get(wiki_link)
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open('{}sp500tickers.pickle'.format(ploc), 'wb') as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers


# save_sp500_tickers()


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


def compile_data():
    '''
    Combines all data sources into a single dataframe

    Parameters
    ==========
    Takes no parameters

    Returns

    sp500_joined_adj_closes.csv : csv file
        Returns, and saves, a csv file with the Adj close data for all
        companies in the S&P 500
    '''

    with open('{}sp500tickers.pickle'.format(ploc), 'rb') as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        df = pd.read_csv('{}{}.csv'.format(dloc, ticker))
        df.set_index('Date', inplace=True)

        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)

    print(main_df.head())
    main_df.to_csv('{}sp500_joined_adj_closes.csv'.format(sloc))


compile_data()
