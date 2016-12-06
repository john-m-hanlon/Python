'''
Import the modules necessary for analysis
'''
import quandl
import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
from sklearn import svm, preprocessing, cross_validation
style.use('fivethirtyeight')



'''
Set file pathes and API keys
'''
auth_key = '-ksDg4as87XubzhJVyJQ'
ticker_path = '/Users/JohnHanlon/Desktop/Python/GA Project/'

ticker_pickle = 'ticker_data.pickle'
ticker_data_and_indicator_pickle = 'ticker_data_and_indicator_pickle.pickle'

# list_of_tickers = 'IGM Tickers.csv'
list_of_tickers = 'IGM Tickers Partial.csv'

ETF = 'SPGSTI'



'''
Create label for ML classifier
'''

def create_labels(cur_index, fut_index):
	if fut_index > cur_index:
		return 1
	else:
		return 0



'''
Load in data
'''

data = pd.read_pickle('{}{}'.format(ticker_path, ticker_data_and_indicator_pickle))
data = data.pct_change()
data.replace([np.inf, -np.inf], np.nan, inplace=True)
data.dropna(inplace=True)

data['SPGSTI_future'] = data['SPGSTI'].shift(-1)
data.dropna(inplace=True)

data['Label'] = list(map(create_labels, data['SPGSTI'], data['SPGSTI_future']))

print(data)


X = np.array(data.drop(['Label','SPGSTI_future'], 1))
X = preprocessing.scale(X)
y = np.array(data['Label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))

