import re
import pandas as pd
import os
import time
from datetime import datetime
import quandl
from time import mktime
# import matplotlib
# import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


api_key = '-ksDg4as87XubzhJVyJQ'
path = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Machine Learning'\
       '/Machine Learning SKLearn [Sentdex]/intraQuarter/'
key_stats_csv = 'key_stats.csv'
stock_prices_file = 'stock_prices_Nov21.csv'
key_stats_csv_acc = 'key_stats_acc_perf_NO_NA_Nov28.csv'
# key_stats_csv_acc = 'key_stats_acc_perf_W_NA.csv'


def Key_Stats(gather=['Total Debt/Equity',
                      'Trailing P/E',
                      'Price/Sales',
                      'Price/Book',
                      'Profit Margin',
                      'Operating Margin',
                      'Return on Assets',
                      'Return on Equity',
                      'Revenue Per Share',
                      'Market Cap',
                      'Enterprise Value',
                      'Forward P/E',
                      'PEG Ratio',
                      'Enterprise Value/Revenue',
                      'Enterprise Value/EBITDA',
                      'Revenue',
                      'Gross Profit',
                      'EBITDA',
                      'Net Income Avl to Common',
                      'Diluted EPS',
                      'Earnings Growth',
                      'Revenue Growth',
                      'Total Cash',
                      'Total Cash Per Share',
                      'Total Debt',
                      'Current Ratio',
                      'Book Value Per Share',
                      'Cash Flow',
                      'Beta',
                      'Held by Insiders',
                      'Held by Institutions',
                      'Shares Short (as of',
                      'Short Ratio',
                      'Short % of Float',
                      'Shares Short (prior ']):

    print('Starting to run Key Stats...')
    stats_path = '{}_KeyStats'.format(path)
    stock_list = [x[0] for x in os.walk(stats_path)]
    df = pd.DataFrame(columns=['Date',
                               'Unix',
                               'Ticker',
                               'Price',
                               'stock p change',
                               'sp500',
                               'sp500 p change',
                               'difference',
                               'status',
                               'DE Ratio',
                               'Trailing P/E',
                               'Price/Sales',
                               'Price/Book',
                               'Profit Margin',
                               'Operating Margin',
                               'Return on Assets',
                               'Return on Equity',
                               'Revenue Per Share',
                               'Market Cap',
                               'Enterprise Value',
                               'Forward P/E',
                               'PEG Ratio',
                               'Enterprise Value/Revenue',
                               'Enterprise Value/EBITDA',
                               'Revenue',
                               'Gross Profit',
                               'EBITDA',
                               'Net Income Avl to Common',
                               'Diluted EPS',
                               'Earnings Growth',
                               'Revenue Growth',
                               'Total Cash',
                               'Total Cash Per Share',
                               'Total Debt',
                               'Current Ratio',
                               'Book Value Per Share',
                               'Cash Flow',
                               'Beta',
                               'Held by Insiders',
                               'Held by Institutions',
                               'Shares Short (as of',
                               'Short Ratio',
                               'Short % of Float',
                               'Shares Short (prior '])

    sp500_df = quandl.get('EOD/SPY', authtoken=api_key)
    stock_df = pd.read_csv('{}{}'.format(path, stock_prices_file))

    ticker_list = []

    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("/")[-1]
        ticker_list.append(ticker)

        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = '{}/{}'.format(each_dir, file)
                source = open(full_file_path, 'r', encoding='utf8').read()
                try:
                    value_list = []
                    for each_data in gather:
                        try:
                            rx = '.*?(\d{1,8}\.\d{1,8}M?B?|N/A)%?'
                            regex = re.escape(each_data) + r'{}'.format(rx)
                            value = re.search(regex, source)
                            value = (value.group(1))

                            if 'B' in value:
                                value = float(value.
                                              replace('B', '')) * 1000000000

                            elif 'M' in value:
                                value = float(value.replace('M', '')) * 1000000

                            elif 'K' in value:
                                value = float(value.replace('K', '')) * 1000

                            value_list.append(value)

                        except:
                            value = 'N/A'
                            value_list.append(value)
# lets get the sp500 values and dates to start
                    try:
                        sp500_date = datetime.fromtimestamp(unix_time)\
                                             .strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_date)]
                        sp500_value = float(row['Adj_Close'])
                    except:

                        try:
                            sp500_date = datetime.fromtimestamp(unix_time -
                                                                259200)\
                                                 .strftime('%Y-%m-%d')
                            row = sp500_df[(sp500_df.index == sp500_date)]
                            sp500_value = float(row['Adj_Close'])
                        except Exception as e:
                            print('ERROR IN SECTION 1: ', str(e))

                    one_year_later = int(unix_time + 31536000)

#  now we are getting the SP 500 values 1 year later
                    try:
                        sp500_1y = datetime.fromtimestamp(one_year_later)\
                                           .strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df.index == sp500_1y)]
                        sp500_1y_value = float(row['Adj_Close'])
                    except Exception as e:

                        try:
                            sp500_1y = datetime.fromtimestamp(one_year_later -
                                                              259200)\
                                               .strftime('%Y-%m-%d')
                            row = sp500_df[(sp500_df.index == sp500_1y)]
                            sp500_1y_value = float(row['Adj_Close'])
                        except Exception as e:
                            print('ERROR IN SECTION 2: ', str(e))

#  getting the stock price one year later
                    try:
                        stock_price_1y = datetime.fromtimestamp(
                            one_year_later).strftime('%Y-%m-%d')
                        row = stock_df[(stock_df['Date'] ==
                                        stock_price_1y)][ticker]
                        stock_1y_value = round(float(row), 2)

                    except Exception as e:
                        try:
                            stock_price_1y = datetime.fromtimestamp(
                                one_year_later - 259200).strftime('%Y-%m-%d')
                            row = stock_df[(stock_df['Date'] ==
                                            stock_price_1y)][ticker]
                            stock_1y_value = round(float(row), 2)
                        except Exception as e:
                            print('ERROR IN SECTION 3: ', ticker, str(e))

#  now we are gettin the stock price
                    try:
                        stock_price = datetime.fromtimestamp(
                            unix_time).strftime('%Y-%m-%d')
                        row = stock_df[(stock_df['Date'] ==
                                        stock_price)][ticker]
                        stock_price = round(float(row), 2)
                    except Exception as e:
                        try:
                            stock_price = datetime.fromtimestamp(
                                unix_time - 259200).strftime('%Y-%m-%d')
                            row = stock_df[(stock_df['Date'] ==
                                            stock_price)][ticker]
                            stock_price = round(float(row), 2)
                        except Exception as e:
                            print('ERROR IN SECTION 4: ', ticker, str(e))

                    stock_p_change = round(((stock_1y_value - stock_price) /
                                           stock_price * 100.0), 2)

                    sp500_p_change = round(((sp500_1y_value - sp500_value) /
                                           sp500_value * 100.0), 2)

                    difference = stock_p_change - sp500_p_change

                    if difference > 0:
                        status = 'outperform'
                    else:
                        status = 'underperform'

                    if value_list.count('N/A') > 0:
                        pass

                    else:
                        df = df.append({'Date': date_stamp,
                                        'Unix': unix_time,
                                        'Ticker': ticker,
                                        'Price': stock_price,
                                        'stock p change': stock_p_change,
                                        'sp500': sp500_value,
                                        'sp500 p change': sp500_p_change,
                                        'difference': difference,
                                        'status': status,
                                        'DE Ratio': value_list[0],
                                        'Trailing P/E': value_list[1],
                                        'Price/Sales': value_list[2],
                                        'Price/Book': value_list[3],
                                        'Profit Margin': value_list[4],
                                        'Operating Margin': value_list[5],
                                        'Return on Assets': value_list[6],
                                        'Return on Equity': value_list[7],
                                        'Revenue Per Share': value_list[8],
                                        'Market Cap': value_list[9],
                                        'Enterprise Value': value_list[10],
                                        'Forward P/E': value_list[11],
                                        'PEG Ratio': value_list[12],
                                        'Enterprise Value/Revenue':
                                        value_list[13],
                                        'Enterprise Value/EBITDA':
                                        value_list[14],
                                        'Revenue': value_list[15],
                                        'Gross Profit': value_list[16],
                                        'EBITDA': value_list[17],
                                        'Net Income Avl to Common':
                                        value_list[18],
                                        'Diluted EPS': value_list[19],
                                        'Earnings Growth': value_list[20],
                                        'Revenue Growth': value_list[21],
                                        'Total Cash': value_list[22],
                                        'Total Cash Per Share': value_list[23],
                                        'Total Debt': value_list[24],
                                        'Current Ratio': value_list[25],
                                        'Book Value Per Share': value_list[26],
                                        'Cash Flow': value_list[27],
                                        'Beta': value_list[28],
                                        'Held by Insiders': value_list[29],
                                        'Held by Institutions': value_list[30],
                                        'Shares Short (as of': value_list[31],
                                        'Short Ratio': value_list[32],
                                        'Short % of Float': value_list[33],
                                        'Shares Short (prior ': value_list[34]
                                        }, ignore_index=True)

                except:
                    pass

    df.to_csv('{}{}'.format(path, key_stats_csv_acc))
    print('Finished running Key Stats...')


Key_Stats()
