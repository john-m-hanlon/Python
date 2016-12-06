import pandas as pd
import os
import time
from datetime import datetime

path = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Machine Learning/Machine Learning SKLearn [Sentdex]/intraQuarter/'

def Key_Stats(gather='Total Debt/Equity (mrq)'):
	stats_path = '{}_KeyStats'.format(path)
	stock_list = [x[0] for x in os.walk(stats_path)]
	df = pd.DataFrame(columns=['Date','Unix','Ticker','DE Ratio']) 
	for each_dir in stock_list[1:]: #the first output is the root directory, do not want this
		each_file = os.listdir(each_dir)
		ticker = each_dir.split("/")[-1]
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
					value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
					df = df.append({'Date':date_stamp, 'Unix':unix_time, 'Ticker':ticker, 'DE Ratio':value}, ignore_index=True)
				except Exception as e:
					pass
				# print('{}:{}'.format(ticker, value))

				# time.sleep()
	save = gather.replace('','').replace(')','').replace('(','').replace('/','')+('.csv')
	df.to_csv('{}{}'.format(path, save))

Key_Stats()


