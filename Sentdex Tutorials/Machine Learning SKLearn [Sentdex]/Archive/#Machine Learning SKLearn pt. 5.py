#Machine Learning SKLearn pt. 5

import pandas as pd 
import os 
import time 
from datetime import datetime

path = '/Users/JohnHanlon/Desktop/Summer Learning/Python/Machine Learning SKLearn [Sentdex]/intraQuarter'

def Key_Stats(gather='Total Debt/Equity (mrq)'):
	statspath = path+'/_KeyStats'
	stock_list = [x[0] for x in os.walk(statspath)]
	df = pd.DataFrame(columns=['Data','Unix','Ticker','DE Ratio'])

	for each_dir in stock_list[1:5]:
		each_file = os.listdir(each_dir)
		ticker = each_dir.split('/')[-1]
		if len(each_file) > 0:
			for file in each_file:
				date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
				unix_time = time.mktime(date_stamp.timetuple())
				full_file_path = each_dir+'/'+file
				source = open(full_file_path,'r',encoding='utf8').read()
				try:
					value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
					print(ticker+':',value)	
					
				except Exception as e:
					pass


Key_Stats()