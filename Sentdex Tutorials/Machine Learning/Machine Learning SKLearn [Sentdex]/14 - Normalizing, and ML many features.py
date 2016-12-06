import numpy as np
import pandas as pd
from sklearn import preprocessing, svm
from matplotlib import style

style.use('fivethirtyeight')

path = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Machine Learning/'\
       'Machine Learning SKLearn [Sentdex]/intraQuarter/'

key_stats_csv = 'key_stats.csv'


FEATURES = ['DE Ratio',
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
            'Shares Short (prior ']


def Build_Data_Set():
    data_df = pd.read_csv('{}{}'.format(path, key_stats_csv))

    #  data_df = data_df[:100]

    #  data[features], means we take the two features of data, DE Ratio and
    #  Trailing PE and converts them to just those values, and then tolist()
    #  converts to a python list

    X = np.array(data_df[FEATURES].values)
    y = (data_df['status'].replace('underperform', 0).replace('outperform', 1)
                                                     .values.tolist())

    X = preprocessing.scale(X)
    return X, y


def Analysis():

    test_size = 1000

    X, y = Build_Data_Set()

    print(len(X))

    clf = svm.SVC(kernel='linear', C=1.0)
    clf.fit(X[:test_size], y[:test_size])
    #  clf.fit(X, y)

    correct_count = 0

    for x in range(1, test_size + 1):
        if clf.predict(X[-x])[0] == y[-x]:
            correct_count += 1

    print('Accuray: {}'.format((correct_count / test_size) * 100))


Analysis()
