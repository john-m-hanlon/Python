import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = '-ksDg4as87XubzhJVyJQ'

def mortgage_30year():
	df = quandl.get('FMAC/MORTG', trim_start='1975-01-01', authtoken=api_key)
	df.columns = ['M30']
	df['M30'] = (df['M30'] - df['M30'][0]) / df['M30'][0] * 100.0
	#df = df.resample('M').mean()

	df = df.resample('M').sum()
	return df


def state_list():
	fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	return fiddy_states[0][0][1:]

def grab_initial_data_set():
	states = state_list()
	main_df = pd.DataFrame()


	for abbv in states:
		query = 'FMAC/HPI_'+str(abbv)
		df = quandl.get(query, authtoken=api_key)
		df.columns = [str(abbv)]
		df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0
		
		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df)

	print(main_df.head())

	pickle_out = open('fiddy_states3.pickle', 'wb')
	pickle.dump(main_df, pickle_out)
	pickle_out.close()


def HPI_Benchmark():
	df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
	df.columns = ['United States']
	df['United States'] = (df['United States'] - df['United States'][0]) / df['United States'][0] * 100.0
	return df 
   

#grab_initial_data_set()

fig = plt.figure()
ax1 = plt.subplot2grid((2, 1), (0,0))
ax2 = plt.subplot2grid((2, 1), (1,0), sharex=ax1)


print('pulling HPI for the 50 states...')
HPI_data = pd.read_pickle('/Users/JohnHanlon/Desktop/Summer Learning/Python/Data Analysis & Pandas [SENTDEX]/fiddy_states3.pickle')
print(HPI_data.head())

HPI_data['TX12MA'] = HPI_data['TX'].rolling(12).mean() #pd.rolling_mean(HPI_data['TX'],12)
HPI_data['TX12STD'] = HPI_data['TX'].rolling(12).std() #pd.rolling_std(HPI_data['TX'],12)
print(HPI_data[['TX', 'TX12MA', 'TX12STD']].head())

HPI_data[['TX', 'TX12MA']].plot(ax=ax1)
HPI_data['TX12STD'].plot(ax=ax2)

TX_AK_12corr = HPI_data['TX'].rolling(12).corr(HPI_data['AK'])

HPI_data['TX'].plot(ax=ax1, label='TX HPI')
HPI_data['AK'].plot(ax=ax1, label='AK HPI')
ax1.legend(loc=4)

TX_AK_12corr.plot(ax=ax2, label='TX_AK_12corr')


plt.legend(loc=4)
plt.show()

# always resample to a timeframe that is larger than what you already have, otherwise it wont create more data for you
#can resample down to nanoseconds with python 
# take unstructured data and make it slightly more structured

print('calculating 30-year Mortgage rates...')
m30 = mortgage_30year()
print(m30.head())


print('calculating HPI Benchmark...')
HPI_bench = HPI_Benchmark()
print(HPI_bench.head())


print('joining 30 year mortage data into 50 states data...')
state_HPI_M30 = HPI_data.join(m30)
#print(state_HPI_M30.head())

print(state_HPI_M30.corr().describe())


# print(m30)
# print(state_HPI_M30.head())