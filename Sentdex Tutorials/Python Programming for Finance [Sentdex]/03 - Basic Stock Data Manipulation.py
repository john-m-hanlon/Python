""" This file contains code for use with "Python Programming for Finance" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

floc = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Python ' \
       'Programming for Finance [Sentdex]/Data Examples/'
ftype = '.csv'
security = 'TSLA'

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

# df = web.DataReader(security, 'yahoo', start, end)
# df.to_csv('{}{}{}'.format(floc, security, ftype))
# df.head()

df = pd.read_csv('{}{}{}'.format(floc, security, ftype), parse_dates=True,
                 index_col=0)

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df.dropna(inplace=True)

print(df.head())

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.plot(df.index, df['Volume'])

plt.show()
