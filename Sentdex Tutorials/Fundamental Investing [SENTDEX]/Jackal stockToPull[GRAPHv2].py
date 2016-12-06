### IMPORTS ###
import urllib2
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick
import matplotlib
import pylab
matplotlib.rcParams.update({'font.size': 9})





### STOCKS ###






### RELATIVE STRENGTH INDEX ###
def rsiFunc(prices, n=14):
	deltas = np.diff(prices)
	seed = deltas[:n+1]
	up = seed[seed>=0].sum()/n
	down = -seed[seed<0].sum()/n
	rs = up/down
	rsi = np.zeros_like(prices)
	rsi[:n] = 100. - 100./(1.+rs)
	for i in range(n, len(prices)):
		delta = deltas[i-1]
		if delta > 0:
			upval = delta
			downval = 0.
		else:
			upval = 0.
			downval = -delta
		up = (up*(n-1)+upval)/n
		down = (down*(n-1)+downval)/n
		rs = up/down
		rsi[i] = 100. - 100./(1.+rs)
	return rsi





### SIMPLE MOVING AVERAGE ###
def movingaverage(values,window):
	weights = np.repeat(1.0, window)/window
	smas = np.convolve(values, weights, 'valid')
	return smas





### EXPONENTIAL MOVING AVERAGE ###
def ExpMovingAverage(values,window):
	weights = np.exp(np.linspace(-1., 0., window))
	weights /= weights.sum()
	a = np.convolve(values, weights, mode='full')[:len(values)]
	a[:window] = a[window]
	return a




### MOVING AVERAGE CONVERGENCE DIVERGENCE (MACD) ###
def computeMACD(x, slow=26, fast=12):
	emaslow = ExpMovingAverage(x, slow)
	emafast = ExpMovingAverage(x, fast)
	return emaslow, emafast, emafast - emaslow





### GRAPH ###
def graphData(stock,MA1,MA2):
	try:
		try:
			print 'pulling data on',stock
			urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
			stockFile = []
			try:
				sourceCode = urllib2.urlopen(urlToVisit).read()
				splitSource = sourceCode.split('\n')
				for eachLine in splitSource:
					splitLine = eachLine.split(',')
					if len(splitLine)==6:
						if 'values' not in eachLine:
							stockFile.append(eachLine)

			except Exception, e:
				print str(e),'failed to organized pulled data'

		except Exception, e:
			print str(e), 'failed to pull price data'		

		date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile,delimiter=',',unpack=True,converters={ 0: mdates.strpdate2num('%Y%m%d')})

### CANDLESTICK ###
		x = 0
		y = len(date)
		candleAr = []
		while x < y:
			appendLine = date[x],openp[x],closep[x],highp[x],lowp[x],volume[x]
			candleAr.append(appendLine)
			x+=1

		Av1 = movingaverage(closep, MA1)
		Av2 = movingaverage(closep, MA2)

		SP = len(date[MA2-1:])

		label1=str(MA1)+' SMA'
		label2=str(MA2)+' SMA'

		fig = plt.figure(facecolor='#07000d')

		ax1 = plt.subplot2grid((6,4), (1,0), rowspan=4, colspan=4, axisbg='#07000d')
		candlestick(ax1, candleAr[-SP:], width=1, colorup='#53c156', colordown='#ff1717')		

		ax1.plot(date[-SP:],Av1[-SP:],'#e1edf9',label=label1, linewidth=1.5)
		ax1.plot(date[-SP:],Av2[-SP:],'#4ee6fd',label=label2, linewidth=1.5)
		ax1.grid(True, color='w')
		ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
		ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
		plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='both'))
		ax1.yaxis.label.set_color('w')
		ax1.spines['bottom'].set_color('#5998ff')
		ax1.spines['top'].set_color('#5998ff')
		ax1.spines['left'].set_color('#5998ff')
		ax1.spines['right'].set_color('#5998ff')
		ax1.tick_params(axis='y', colors='w')
		plt.ylabel('Stock price')
		
		



### LEGEND ###
		maLeg = plt.legend(loc=9, ncol=2, prop={'size': 7}, fancybox=True, borderaxespad=0.)
		maLeg.get_frame().set_alpha(0.4)
		textEd = pylab.gca().get_legend().get_texts()
		pylab.setp(textEd[0:5], color = 'w')





### RELATIVE STRENGTH INDEX ###
		ax0 = plt.subplot2grid((6,4), (0,0), sharex=ax1, rowspan=1, colspan=4, axisbg='#07000d')
		rsiCol = '#c1f9f7'
		posCol = '#386d14'
		negCol = '#5f2020'
		midCol = '#bdbdb1'
		rsi = rsiFunc(closep)
		ax0.plot(date[-SP:],rsi[-SP:],rsiCol,linewidth=1.5)
		ax0.axhline(70, color = negCol)
		ax0.axhline(30, color = posCol)
		ax0.axhline(50, color = midCol)
		ax0.fill_between(date[-SP:],rsi[-SP:], 70, where=(rsi[-SP:]>=70), facecolor=negCol, edgecolor=negCol)
		ax0.fill_between(date[-SP:],rsi[-SP:], 30, where=(rsi[-SP:]<=30), facecolor=posCol, edgecolor=posCol)
		ax0.spines['bottom'].set_color('#5998ff')
		ax0.spines['top'].set_color('#5998ff')
		ax0.spines['left'].set_color('#5998ff')
		ax0.spines['right'].set_color('#5998ff')
		ax0.text(0.015, 0.95, 'RSI (14)', va='top', color='w', transform=ax0.transAxes)
		ax0.tick_params(axis='x', colors='w')
		ax0.tick_params(axis='y', colors='w')
		ax0.set_yticks([30,70])
		ax0.yaxis.label.set_color('w')
		#plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='lower'))





### VOLUME ###
		volumeMin = 0

		ax1v = ax1.twinx()
		ax1v.fill_between(date[-SP:],volumeMin, volume[-SP:], facecolor='#00ffe8', alpha=.5)
		ax1v.axes.yaxis.set_ticklabels([])
		ax1v.grid(False)
		ax1v.spines['bottom'].set_color('#5998ff')
		ax1v.spines['top'].set_color('#5998ff')
		ax1v.spines['left'].set_color('#5998ff')
		ax1v.spines['right'].set_color('#5998ff')
		ax1v.set_ylim(0, 2*volume.max())
		ax1v.tick_params(axis='x', colors='w')
		ax1v.tick_params(axis='y', colors='w')	





### MACD ###
		ax2 = plt.subplot2grid((6,4), (5,0), sharex=ax1, rowspan=1, colspan=4, axisbg='#07000d')
		fillcolor = '#00ffe8'
		nslow = 26
		nfast = 12
		nema = 9

		emaslow, emafast, macd = computeMACD(closep)
		ema9 = ExpMovingAverage(macd, nema)

		ax2.plot(date[-SP:], macd[-SP:], color='#e1edf9', lw=2)
		ax2.plot(date[-SP:], ema9[-SP:], color='#4eeffd', lw=1)
		ax2.fill_between(date[-SP:], macd[-SP:] -ema9[-SP:], 0, alpha=0.5, facecolor=fillcolor, edgecolor=fillcolor)
		ax2.text(0.015, 0.95, 'MACD (12, 26, 9)', va='top', color='w', transform=ax2.transAxes)
		ax2.spines['bottom'].set_color('#5998ff')
		ax2.spines['top'].set_color('#5998ff')
		ax2.spines['left'].set_color('#5998ff')
		ax2.spines['right'].set_color('#5998ff')
		ax2.tick_params(axis='x', colors='w')
		ax2.tick_params(axis='y', colors='w')	
		ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='upper'))

		for label in ax2.xaxis.get_ticklabels():
			label.set_rotation(45)





###
		plt.suptitle(stock + ' Stock Price', color='w')
		
		plt.setp(ax0.get_xticklabels(), visible=False)
		plt.setp(ax1.get_xticklabels(), visible=False)
		plt.subplots_adjust(left=.09, bottom=.14, right=.94, top=.95, wspace=.20, hspace=.00)
		plt.show()
		fig.savefig(stock + '.png',facecolor=fig.get_facecolor())

	except Exception, e:
		print 'failed main loop', str(e)






####
while True:
	stockToUse = raw_input('Stock to chart: ')
	graphData(stockToUse,12,26)