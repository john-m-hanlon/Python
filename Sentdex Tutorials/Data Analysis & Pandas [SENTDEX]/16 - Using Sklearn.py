import quandl
import numpy as np
import pandas as pd
from sklearn import svm, preprocessing, cross_validation
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
style.use('fivethirtyeight')

api_key = '-ksDg4as87XubzhJVyJQ'


def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0

#create your own function
def moving_average(values):
    return mean(values)

        
        
housing_data = pd.read_pickle('/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Data Analysis & Pandas [SENTDEX]/HPI.pickle')
housing_data = housing_data.pct_change()


housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data['US_HPI_future'] = housing_data['United States'].shift(-1)


housing_data.dropna(inplace=True)
print(housing_data[['US_HPI_future', 'United States']].head())

housing_data['Label'] = list(map(create_labels, housing_data['United States'], housing_data['US_HPI_future']))
print(housing_data.head())


X = np.array(housing_data.drop(['Label', 'US_HPI_future'], 1))
X = preprocessing.scale(X)

y = np.array(housing_data['Label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

c_score = clf.score(X_test, y_test) 
print(c_score)








