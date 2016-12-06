import quandl
import pandas as pd
import pickle

api_key = '-ksDg4as87XubzhJVyJQ'
f_path = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Data Analysis & Pandas [SENTDEX]/'


def state_list():
	fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

	return fiddy_states[0][0][1:]

print('#'*50)
print(quandl.get('FMAC/HPI_NY', authtoken=api_key).head())
print('#'*50)

def grab_initial_data_set():
	states = state_list()
	main_df = pd.DataFrame()


	for abbv in states:
		query = 'FMAC/HPI_'+str(abbv)
		df = quandl.get(query, authtoken=api_key)
		df.columns = [str(abbv)]
		
		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df)

	print(main_df.head())

	pickle_out = open('{}fiddy_states.pickle'.format(f_path), 'wb')
	pickle.dump(main_df, pickle_out)
	pickle_out.close()


#grab_initial_data_set()

pickle_in = open('{}fiddy_states.pickle'.format(f_path),'rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)

HPI_data.to_pickle('{}pickle.pickle'.format(f_path))
HPI_data2 = pd.read_pickle('{}pickle.pickle'.format(f_path))
print(HPI_data2)
