'''
Import the modules necessary for analysis
'''
import quandl
import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')



'''
Set file pathes and API keys
'''
ticker_path = '/Users/JohnHanlon/Desktop/Python/GA Project/'
auth_key = '-ksDg4as87XubzhJVyJQ'



'''
Pull a list of tickers in the IGM ETF
'''
def ticker_list():
    df = pd.read_csv('{}IGM Tickers.csv'.format(ticker_path))
    # print(df['Ticker'])
    return df['Ticker']



'''
Pull the historical prices for the securities within Ticker List
'''
def grab_constituent_data():
    
    tickers = ticker_list()
    main_df = pd.DataFrame()
    total_len = len(tickers)
    count = 0
    for abbv in tickers:
        query = 'EOD/{}'.format(str(abbv))
        df = quandl.get(query, authtoken=auth_key)
        print('Competed the query for {}'.format(query))
        
        # df['{} Adj_Close'.format(str(abbv))] = df['Adj_Close'].copy()
        # df = df['{} Adj_Close'.format(str(abbv))].to_frame()
        # print('Completed the column adjustment for {}'.format(str(abbv)))
        
        df['Adj_Close'] = (df['Adj_Close'] - df['Adj_Close'][0]) / df['Adj_Close'][0] * 100.0
        df.rename(columns={'Adj_Close':str(abbv)}, inplace=True)
        df = df[str(abbv)]
        return df
        
        #LET'S SEE IF THE ABOVE WORKS AND WE CAN PULL THE PCT DATA...
        
        
        
        # df[abbv] = df['Adj_Close'].copy()
        # df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0
        # print('Completed the column adjustment for {}'.format(str(abbv)))
        '''
        Show us how many securites we have joined into the dataframe
        '''
        count += 1
        perc_comp = (count/total_len)*100.0
        print('We have pulled {} securities and are {} complete...'.format(count, perc_comp)))
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            
    print(main_df.head())
    
    '''
    Pickle output data so that it can be retrieved faster at a later date
    '''
    
    pickle_out = open('{}ticker_data.pickle'.format(ticker_path), 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

    

'''
Print output data and run fetch function
'''

grab_constituent_data()

'''
Define a function which pulls the historical data for the ETF and returns the percent change in a dataframe   
'''
def ETF_benchmark():
    ticker = 'EOD/IGM'
    df = quandl.get(ticker, authtoken=auth_key)
    df['IGM'] = (df['Adj_Close'] - df['Adj_Close'][0]) / df['Adj_Close'][0] * 100.0
    df = df['IGM']
    return df
    

    
    






