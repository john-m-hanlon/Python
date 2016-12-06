'''
Import the modules necessary for analysis
'''
import quandl
import pickle
import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
# style.use('ggplot')



'''
Set file pathes and API keys / pickle file names / csvs to iterate / benchmark symbol / data start date
'''
auth_key = '-ksDg4as87XubzhJVyJQ'
ticker_path = '/Users/JohnHanlon/Desktop/Python/GA Project/'

ticker_pickle = 'ticker_data.pickle'
ticker_data_and_indicator_pickle = 'ticker_data_and_indicator_pickle.pickle'

# list_of_tickers = 'IGM Tickers.csv'
list_of_tickers = 'IGM Tickers Partial.csv'

bench = 'XLK'
start_date = '2014-06-02'



'''
Pull a list of tickers in the IGM ETF // should probably adjust this reflect the benchmark XLK
'''
def ticker_list():
    df = pd.read_csv('{}{}'.format(ticker_path, list_of_tickers))
    # print(df['Ticker'])
    return df['Ticker']



'''
Pull the historical prices for the securities within Ticker List
'''
def fetch_constituent_data():
    
    tickers = ticker_list()
    main_df = pd.DataFrame()
    total_len = len(tickers)
    count = 0
    
    for abbv in tickers:
        query = 'EOD/{}'.format(str(abbv))
        df = quandl.get(query, trim_start=start_date, authtoken=auth_key)
        # print('Competed the query for {}'.format(query))
         
        #df['Adj_Close'] = (df['Adj_Close'] - df['Adj_Close'][0]) / df['Adj_Close'][0] * 100.0
        df['Adj_Close'] = df['Adj_Close'].pct_change()
        df.rename(columns={'Adj_Close':str(abbv)}, inplace=True)
        df = df[str(abbv)].to_frame()
        df.dropna()
        '''
        Show us how many securites we have joined into the dataframe
        '''
        count += 1
        perc_comp = (count/total_len)*100.0
        print('We just pulled {}, and have pulled {} out of {} securities. We are {}% complete...'.format(abbv, count, total_len, perc_comp))
        
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print('#'*50)
    print('Printing the output of the function: fetch_constituent_data...')
    print('#'*50)     
    print(main_df.head())
    
    '''
    Pickle output data so that it can be retrieved faster at a later date
    '''
    
    pickle_out = open('{}{}'.format(ticker_path, ticker_pickle), 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

    

'''
Print output data and run fetch function
'''
# fetch_constituent_data()



'''
Bring back in the above function with the pickle
'''
pickle_in = open('{}{}'.format(ticker_path, ticker_pickle), 'rb')
ticker_data = pickle.load(pickle_in).dropna()
print('#'*50)
print('Printing the variable ticker_data...')
print('#'*50)
print(ticker_data)



'''
Define a function which pulls the historical data for the ETF and returns the percent change in a dataframe   
'''
def fetch_bench():
    df = quandl.get('EOD/{}'.format(bench), trim_date=start_date, authtoken=auth_key)
    # df[ETF] = (df['Close'] - df['Close'][0]) / df['Close'][0] * 100.0
    df[bench] = df['Close'].pct_change()
    df = df[bench]
    return df



'''
Call the fetched data and comment it out once it has been pickled
'''
# bench_data = fetch_bench()
# print('#'*50)
# print('Printing benchmark data, {}...'.format(bench))
# print('#'*50)
# print(bench_data.head())



'''
Merging data securities data and benchmark data, pickling for later recall, after first run comment out
'''
# ticker_data_and_indicator = ticker_data.join(bench_data)
# ticker_data_and_indicator.to_pickle('{}{}'.format(ticker_path, ticker_data_and_indicator_pickle))



'''
Load in the previously pickled data
'''
pickle_in = open('{}{}'.format(ticker_path, ticker_data_and_indicator_pickle), 'rb')
ticker_data_and_indicator = pickle.load(pickle_in).dropna()



'''
Print the correlation analysis for each security and the describe summary output
'''
print('#'*50)
print('Printing the correlation analysis data...')
print('#'*50)
print(ticker_data_and_indicator.corr())
print(ticker_data_and_indicator.corr().describe())



'''
Plotting the daily % change
'''
# ticker_data_and_indicator.plot()
# plt.legend().remove()
# plt.show()


#maybe resample by month and sum to get % returns?

#determine ranking scheme of securities, 25 long, 25 short
# keep the qty constant
# train over period of time

#
x = 1
y = 3



