import os
import time
from datetime import datetime

path = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/' \
       'Machine Learning/Machine Learning SKLearn [Sentdex]/intraQuarter/'


def Key_Stats(gather='Total Debt/Equity (mrq)'):
    stats_path = '{}/_KeyStats'.format(path)
    stock_list = [x[0] for x in os.walk(stats_path)]
    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                print(date_stamp, unix_time)


Key_Stats()
