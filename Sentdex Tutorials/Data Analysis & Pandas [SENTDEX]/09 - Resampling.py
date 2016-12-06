import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = '-ksDg4as87XubzhJVyJQ'

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
ax1 = plt.subplot2grid((1, 1), (0,0))

HPI_data = pd.read_pickle('fiddy_states3.pickle')

TX1yr = HPI_data['TX'].resample('A').mean()
print(TX1yr.head())

HPI_data['TX'].plot(ax=ax1, label='Monthly TX HPI')
TX1yr.plot(ax=ax1, label='Yearly TX HPI')

plt.legend(loc=4)
plt.show()

# always resample to a timeframe that is larger than what you already have, otherwise it wont create more data for you
#can resample down to nanoseconds with python 
# take unstructured data and make it slightly more structured
