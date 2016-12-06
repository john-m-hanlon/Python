import pandas as pd
import os
import time
from datetime import datetime
import quandl
from time import mktime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import re



api_key = '-ksDg4as87XubzhJVyJQ'

path = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Machine Learning/Machine Learning SKLearn [Sentdex]/intraQuarter/'

def Key_Stats(gather='Total Debt/Equity (mrq)'):
	print('Starting to run Key Stats...')
	stats_path = '{}_KeyStats'.format(path)
	stock_list = [x[0] for x in os.walk(stats_path)]
	df = pd.DataFrame(columns=['Date',
							   'Unix',
							   'Ticker',
							   'DE Ratio',
							   'Price',
							   'stock_p_change'
							   'SP500',
							   'sp500_p_change',
							   'difference',
							   'status']) 

	sp500_df = quandl.get('EOD/SPY', authtoken=api_key)



	ticker_list = []

	for each_dir in stock_list[1:25]: #the first output is the root directory, do not want this
		each_file = os.listdir(each_dir)
		ticker = each_dir.split("/")[-1]
		ticker_list.append(ticker)

		starting_stock_value = False
		starting_sp500_value = False


		if len(each_file) > 0:
			for file in each_file:
				date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
				unix_time = time.mktime(date_stamp.timetuple())
				# print(date_stamp, unix_time)

				full_file_path = '{}/{}'.format(each_dir, file)
				# print(full_file_path)
				source = open(full_file_path, 'r', encoding='utf8').read()
				# print(source)
				try:
					try:
						value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
					except Exception as e:
						try:
							value = float(source.split(gather+':</td>\n<td class="yfnc_tabledata1">')[1].split('</td>')[0])
							# print(str(e), ticker, file)
						except Exception as e:
							pass
							# print(str(e), ticker, file)
							# value = float(source.split(gather+':</td>\n<td class="yfnc_tabledata1">')[1].split('</td>')[0])
							




					try:
						sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')					
						row = sp500_df[(sp500_df.index == sp500_date)]
						sp500_value = float(row['Adj_Close'])
					except:
						sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')					
						row = sp500_df[(sp500_df.index == sp500_date)]
						sp500_value = float(row['Adj_Close'])


					try:
						stock_price = float(source.split('</small><big><b>')[1].split('</b></big>')[0])
						# print('stock price: {}, ticker: {}'.format(stock_price, ticker))
						
					except Exception as e:
						# <span id="yfs_l10_aa">12.04</span>
						try:
							stock_price = (source.split('</small><big><b>')[1].split('</b></big>')[0])
							stock_price = re.search(r'(\d{1,8}\.\d{1,8})', stock_price)
							stock_price = float(stock_price.group(1))
							# print(stock_price)
					
						except Exception as e:
							
							stock_price = (source.split('<span class="time_rtq_ticker">')[1].split('</span>')[0])
							stock_price = re.search(r'(\d{1,8}\.\d{1,8})', stock_price)
							stock_price = float(stock_price.group(1))


							
						

					if not starting_stock_value:
						starting_stock_value = stock_price

					if not starting_sp500_value:
						starting_sp500_value = sp500_value

					stock_p_change = (stock_price - starting_stock_value) / starting_stock_value * 100.0
					sp500_p_change = (sp500_value - starting_sp500_value) / starting_sp500_value * 100.0

					difference = stock_p_change-sp500_p_change

					if difference > 0:
						status = 'outperform'
					else:
						status = 'underperform'




					df = df.append({'Date':date_stamp, 
									'Unix':unix_time, 
									'Ticker':ticker, 
									'DE Ratio':value,
									'Price':stock_price,
									'pct change':stock_p_change,
									'sp500':sp500_value,
									'sp500 pct change':sp500_p_change,
									'difference':difference,
									'status':status }, ignore_index=True)

				except Exception as e:
					pass
					# print(str(e), ticker, file)
				# print('{}:{}'.format(ticker, value))

	for each_ticker in ticker_list:
		try:
			plot_df = df[(df['Ticker'] == each_ticker)]
			plot_df = plot_df.set_index(['Date'])

			if plot_df['status'][-1] == 'underperform':
				color = 'r'
			else:
				color = 'g'




			plot_df['difference'].plot(label=each_ticker, color=color)
			# plt.legend()
		except Exception as e:
			print(str(e))


	plt.show()

	save = gather.replace('','').replace(')','').replace('(','').replace('/','')+('.csv')
	df.to_csv('{}{}'.format(path, save))
	print('Finished running Key Stats...')

	print(df.describe())

Key_Stats()

print
