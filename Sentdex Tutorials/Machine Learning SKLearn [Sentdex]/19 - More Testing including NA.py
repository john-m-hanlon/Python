import numpy as np
import pandas as pd
from sklearn import preprocessing, svm
from matplotlib import style

style.use('fivethirtyeight')

path = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Machine Learning/'\
       'Machine Learning SKLearn [Sentdex]/intraQuarter/'

# key_stats_csv = 'key_stats_acc_perf_W_NA.csv'
key_stats_csv = 'key_stats_acc_perf_NO_NA.csv'

FEATURES = ['DE Ratio',
            'Trailing P/E',
            'Price/Sales',
            'Price/Book',
            'Profit Margin',
            'Operating Margin',
            'Return on Assets',
            #'Return on Equity',
            #'Revenue Per Share',
            #'Market Cap',
            #'Enterprise Value',
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
            #'Total Cash',
            #'Total Cash Per Share',
            #'Total Debt',
            #'Current Ratio',
            #'Book Value Per Share',
            #'Cash Flow',
            #'Beta',
            #'Held by Insiders',
            #'Held by Institutions',
            #'Shares Short (as of',
            #'Short Ratio',
            #'Short % of Float',
            'Shares Short (prior ']


def Build_Data_Set():
    data_df = pd.read_csv('{}{}'.format(path, key_stats_csv))

    #  data_df = data_df[:100]
    data_df = data_df.reindex(np.random.permutation(data_df.index))
    data_df = data_df.replace('NaN', 0).replace('N/A', 0)

    X = np.array(data_df[FEATURES].values)
    y = (data_df['status'].replace('underperform', 0).replace('outperform', 1)
                                                     .values.tolist())

    X = preprocessing.scale(X)
    return X, y


def Analysis():

    test_size = 2500

    X, y = Build_Data_Set()

    print(len(X))

    clf = svm.SVC(kernel='linear', C=1.0)
    clf.fit(X[:test_size], y[:test_size])

    correct_count = 0

    for x in range(1, test_size + 1):
        if clf.predict(X[-x])[0] == y[-x]:
            correct_count += 1

    print('Accuray: {}'.format((correct_count / test_size) * 100))


Analysis()
