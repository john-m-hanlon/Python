import math
import pandas as pd
import numpy as np
import quandl
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import datetime
import matplotlib.pyplot as plt
from matplotlib import style


style.use('fivethirtyeight')

auth_key = '-ksDg4as87XubzhJVyJQ'

f_path = '/Users/JohnHanlon/Desktop/Data/Equities Data/'
security = 'WIKI-GOOGL.csv'


#for when connected to internet for most recent data
df = quandl.get('WIKI/GOOGL', authtoken=auth_key)

#for when working without iternet connection / setting the index
# df = pd.read_csv('{}{}'.format(f_path, security))
# df.set_index(df['Date'], inplace=True)
 
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
df['Label'] = df[forecast_col].shift(-forecast_out)


X = np.array(df.drop(['Label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]



df.dropna(inplace=True)
y = np.array(df['Label'])
y = np.array(df['Label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(
                        X, 
                        y, 
                        test_size=0.2)
                        
clf = LinearRegression() #svm.SVR()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan


last_date = df.iloc[-1].name
# tdelta = datetime.timedelta(days=1)
last_unix = last_date.timestamp() 
one_day = 86400
next_unix = last_unix + one_day
# next_date = last_date + tdelta


for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

print(df.tail())


df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel = ('Date')
plt.ylabel = ('Price')
plt.show( )

