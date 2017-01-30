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
import numpy as np
import pickle
import requests
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

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


# get_data_from_yahoo(reload_sp500=True)

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


# compile_data()


def visualize_data():
    '''
    Outputs a correlation table of all securities in the S&P 500

    Parameters
    ==========
    Takes no parameters

    Returns
    =======
    plt.show() : plot
        Plot of the correlation between each company in the S&P 500

    '''

    df = pd.read_csv('{}sp500_joined_adj_closes.csv'.format(sloc))
    df_corr = df.corr()

    # print(df_corr.head())

    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1, 1)
    plt.tight_layout()
    plt.show()


# visualize_data()


def process_data_for_labels(ticker):
    '''
    Each model generated will be on a per company basis, and each company will
    take into account the pricing data for all other companies in the S&P 500

    Parameters
    ==========
    tickers : str
        company in the S&p 500

    Returns
    =======
    tickers : str
        ticker for all companies in the S&P 500

    df : float
        Adj Close price for all other S&P 500 companies
    '''

    # how many days in the future do we have to make the trading decision
    hm_days = 7
    df = pd.read_csv('{}sp500_joined_adj_closes.csv'.format(sloc), index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days + 1):
        df['{}_{}d'.format(ticker, i)] = ((df[ticker].shift(-i) - df[ticker]) /
                                          df[ticker])

    df.fillna(0, inplace=True)
    return tickers, df


# process_data_for_labels('AAPL')


def buy_sell_hold(*args):
    '''
    Defines the label for buy, sell, and hold

    Parameters
    ==========
    *args : argument
        Becomes an interable of what to pass through

    Returns
    =======
    label : str
        Returns the label buy, sell, or hold for each security


    '''

    cols = [c for c in args]
    requirement = 0.02

    for col in cols:
        if col > requirement:
            return 1

        if col < -requirement:
            return -1

    return 0


def extract_feature_sets(ticker):
    '''
    Mapping the buy_sell_hold(*args) to a dataframe in a new column

    Parameters
    ==========
    ticker : str
        Particular security to be analyzed

    Returns
    =======

    '''

    tickers, df = process_data_for_labels(ticker)
    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                              df['{}_1d'.format(ticker)],
                                              df['{}_2d'.format(ticker)],
                                              df['{}_3d'.format(ticker)],
                                              df['{}_4d'.format(ticker)],
                                              df['{}_5d'.format(ticker)],
                                              df['{}_6d'.format(ticker)],
                                              df['{}_7d'.format(ticker)]
                                              ))
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread:', Counter(str_vals))

    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    X = df_vals.values
    y = df['{}_target'.format(ticker)].values

    return X, y, df


extract_feature_sets('AAPL')
