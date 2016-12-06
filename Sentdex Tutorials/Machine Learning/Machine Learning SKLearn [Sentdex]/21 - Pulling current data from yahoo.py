import urllib.request
import os
import time

path = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Machine Learning' \
       '/Machine Learning SKLearn [Sentdex]/intraQuarter/'


def check_yahoo():
    stats_path = '{}_KeyStats/'.format(path)
    stock_list = [x[0] for x in os.walk(stats_path)]
    for e in stock_list[1:]:
        try:
            e = e.replace(stats_path, '')
            link = 'https://finance.yahoo.com/quote/{}/' \
                   'key-statistics?p={}'.format(e, e)
            response = urllib.request.urlopen(link).read()

            save = '{}forward/{}.html'.format(path, str(e))
            store = open(save, 'w')
            store.write(str(response))
            store.close()

        except Exception as e:
            print(str(e))
            time.sleep(2)


check_yahoo()
