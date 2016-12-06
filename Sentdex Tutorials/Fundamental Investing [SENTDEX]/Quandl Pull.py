import urllib2
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np


def grabQuandl(ticker):

	netIncomeAr = []
	revAr = []

	endLink = 'sort_order=asc&auth_token=-ksDg4as87XubzhJVyJQ'
	try:
		revenue = urllib2.urlopen('https://www.quandl.com/api/v3/datasets/RAYMOND/'+ticker+'_REVENUE_Q.csv?api_key=-ksDg4as87XubzhJVyJQ').read()
		netIncome = urllib2.urlopen('https://www.quandl.com/api/v3/datasets/RAYMOND/'+ticker+'_NET_INCOME_Q.csv?api_key=-ksDg4as87XubzhJVyJQ').read()
		#roc = urllib2.urlopen('https://www.quandl.com/api/v3/datasets/SF1/'+ticker+'_ROIC_ART.csv?api_key=-ksDg4as87XubzhJVyJQ').read()
			
		#print 'Revenue'
		#print revenue
		#print '________________________________'
		#print 'Net Income'
		#print netIncome
		#print '________________________________'
		#print 'Return on Capital'
		#print roc
		#Indicator Description [Return on Invested Capital]: Return on Invested Capital is ratio estimatd by dividing [EBIT] by [INVCAPAVG]. [INVCAP] is calculated as: [DEBT] plus [ASSETS] minus [INTANGIBLES] minus [CASHNEQ] minus [LIABILITIESC]. Please note this calculation method is subject to change.
		
		splitNI = netIncome.split('\n')
		print 'Net Income:'
		for eachNI in splitNI[1:-1]:
			print eachNI
			netIncomeAr.append(eachNI)
		
		print '________________________________'
		splitRev = revenue.split('\n')
		print 'Revenue:'
		for eachRev in splitRev[1:-1]:
			print eachRev
			revAr.append(eachRev)

		incomeDate, income = np.loadtxt(netIncomeAr, delimiter=',',unpack=True,converters={ 0: mdates.strpdate2num('%Y-%m-%d')})

		revenueDate, revenue = np.loadtxt(revAr, delimiter=',', unpack=True,converters={ 0: mdates.strpdate2num('%Y-%m-%d')})

		fig = plt.figure()
		
		ax1 = plt.subplot2grid((6,6),(0,0), rowspan =3, colspan=6)
		ax1.plot(incomeDate, income)
		plt.ylabel('Net Income')
		
		ax2 = plt.subplot2grid((6,6),(3,0), sharex=ax1, rowspan =3, colspan=6)
		ax2.plot(revenueDate, revenue)
		plt.ylabel('Revenue')

		ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
		plt.subplots_adjust(hspace=0.90)

		plt.show()



	except Exception, e:
		print 'failed the main quandl loop for reason of',str(e)

grabQuandl('YHOO')