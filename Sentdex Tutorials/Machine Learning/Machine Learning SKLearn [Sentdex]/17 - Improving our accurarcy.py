import pandas as pd
import os
import quandl
import time

api_key = '-ksDg4as87XubzhJVyJQ'
path = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Machine Learning/'\
       'Machine Learning SKLearn [Sentdex]/intraQuarter/'
stocklist = '_KeyStats'
q = 'EOD/'
# op = 'stock_prices.csv'
op = 'stock_prices_Nov29.csv'


def stock_prices():
    df = pd.DataFrame()
    statspath = '{}{}'.format(path, stocklist)
    stock_list = [x[0] for x in os.walk(statspath)]

    for each_dir in stock_list[1:]:
        try:
            ticker = each_dir.split('/')[-1]
            query = '{}{}'.format(q, ticker)
            data = quandl.get(query, trim_start='2003-11-21',
                              trim_end='2016-11-21',
                              authtoken=api_key)
            data[ticker] = data['Adj_Close']
            df = pd.concat([df, data[ticker]], axis=1)
        except Exception as e:
            print(str(e), ticker)

    df.to_csv('{}{}'.format(path, op))


stock_prices()
