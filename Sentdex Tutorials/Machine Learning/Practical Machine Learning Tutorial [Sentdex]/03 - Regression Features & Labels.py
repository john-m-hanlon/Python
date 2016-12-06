import math
import pandas as pd
import numpy as np
import quandl
from sklearn import preprocessing


auth_key = '-ksDg4as87XubzhJVyJQ'

f_path = '/Users/JohnHanlon/Desktop/Data/Equities Data/'
security = 'WIKI-GOOGL.csv'


#for when connected to internet for most recent data
# df = quandl.get('WIKI/GOOGL', authtoken=auth_key)

#for when working without iternet connection / setting the index
df = pd.read_csv('{}{}'.format(f_path, security))
df.set_index(df['Date'], inplace=True)
 
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close',
         'Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['Label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

print(df.head())
