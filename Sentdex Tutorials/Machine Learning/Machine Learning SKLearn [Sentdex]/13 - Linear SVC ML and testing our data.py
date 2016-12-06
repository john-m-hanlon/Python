import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import pandas as pd
from matplotlib import style

style.use('fivethirtyeight')

path = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Machine Learning/' \
       'Machine Learning SKLearn [Sentdex]/intraQuarter/'
key_stats_csv = 'key_stats.csv'


def Build_Data_Set(features=['DE Ratio',
                             'Trailing P/E']):
    data_df = pd.read_csv('{}{}'.format(path, key_stats_csv))

    # data_df = data_df[:100]

    #  data[features], means we take the two features of data, DE Ratio and
    #  Trailing PE and converts them to just those values, and then tolist()
    #  converts to a python list
    X = np.array(data_df[features].values)
    y = (data_df['status'].replace('underperform', 0).replace('outperform', 1).
         values.tolist())

    return X, y


def Analysis():
    X, y = Build_Data_Set()

    clf = svm.SVC(kernel='linear', C=1.0)
    clf.fit(X, y)

    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(min(X[:, 0]), max(X[:, 0]))
    yy = a * xx - clf.intercept_[0] / w[1]

    h0 = plt.plot(xx, yy, 'k-', label='non-weighted')

    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.ylabel('Trailing PE Ratio')
    plt.xlabel('DE Ratio')
    plt.legend()

    plt.show()


Analysis()
