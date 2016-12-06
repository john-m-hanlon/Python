import math

'''
The below are the keywords in python3

False      class      finally
None       continue   for
True       def        from
and        del        global
as         elif       if
assert     else       import     pass
break      except     in         raise
is         return
lambda     try
nonlocal   while
not        with
or         yield
'''

pi = math.pi

x = y = 1
print(x*y)

#The volume of a sphere with radius r is 4 πr3. What is the volume of a sphere with radius 5?
print(pi)
r = 5
volume = (4/3)*(pi)*(r**3)
print(volume)

'''
Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
Shipping costs $3 for the first copy and 75 cents for each additional copy. 
What is the total wholesale cost for 60 copies?
'''

coverPrice = 24.95
discount = .4
discountPrice = coverPrice * (1 - discount)
print('The discount price is:',discountPrice)

n = 60
shippingCost = (3 + (.75)*(n-1))
print('The shipping cost for 60 books is:',shippingCost)

wholesaleCost = (n * discountPrice) + shippingCost
print(wholesaleCost)


'''
If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
'''

import numpy as np


timeStart = [6,52,00]
easy = [0,8,15]
tempo = [0,7,12]
easyQty = 2
tempoQty = 3
outputEasy = np.multiply(easy,easyQty)
outputTempo = np.multiply(tempo,tempoQty)
print(outputEasy)
print(outputTempo)
totalTime = outputEasy + outputTempo
print(totalTime)
endTime = timeStart + totalTime
print(endTime)

if endTime[2] > 59:
	endTime2 = [endTime[0],endTime[1]+1,endTime[2] - 60]
	print(endTime2)
	if endTime2[1] > 59:
		endTimeFinal = [endTime2[0]+1,endTime2[1]-60,endTime2[2]]
		print(endTimeFinal)




