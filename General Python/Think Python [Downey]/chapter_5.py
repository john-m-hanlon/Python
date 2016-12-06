minutes = 105
print(minutes/60)

hours = minutes // 60
print(hours)

remainder = minutes - hours * 60
print(remainder)

x = 24
y = 8

# the %, modulus operator, divides the two variables and returns the remainder
print('The remainder of x / y is:', x % y,'thus...')
if x % y == 0:
	print('x is divisible by y')

else:
	print('x is not divisible by y')

print(x % 10)
print(x % 100)
print(x % 10000)

#Booleans
print(5 == 5)
print(5 == 6)


# The == operator is one of the relational operators; the others are:
# x != y ...x is not equal to y
# x > y ....x is greater than y
# x < y ....x is less than y
# x >= y ...x is greater than or equal to y 
# x <= y ...x is less than or equal to y
print('-----------------')
print('Logical Operators')
print('-----------------')

n = 9
print(n%2 == 0 or n%3 == 0)

x = 10
y = 12
print(not(x > y))


if x > 0:
	print('x is positive')

x = -2
if x < 0:
	pass
	#To do: need to handle negative values!

from random import *


x = randint(1,10000)
print(x)
if x % 2 == 0:
	print('x is even')

else:
	print('x is odd')



print('-----------------')
print('Recurrsion')
print('-----------------')

def countdown(n):
	if n <= 0:
		print('Blastoff!')
	else:
		print(n)
		countdown(n-1)

countdown(5)

def print_n(s, n):
	if n <= 0:
		return
	print(s)
	print_n(s, n-1)

print_n('John', 1)

print('-----------------')
print('Keyboard input')
print('-----------------')



prompt = 'What is the airspeed velocity of an african swallow? '
#speed = input(prompt)
#print(speed,'test')




'''
Exercise 5.1. The time module provides a function, also named time, that returns the current 
Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. 
On UNIX systems, the epoch is 1 January 1970.
>>> import time
>>> time.time()
1437746094.5735958
Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, 
plus the number of days since the epoch.
'''

import time

epoch = time.time()
myDate = int(epoch)
num_days = myDate // 3600 // 24
print(num_days, 'days since epoch')

midnight_on_mydate = num_days * 24 * 3600
seconds_since_midnight = myDate - midnight_on_mydate

hours = seconds_since_midnight // 3600
minutes = (seconds_since_midnight - (hours * 3600)) // 60
seconds = seconds_since_midnight - (hours * 3600 + minutes * 60)

time_of_day = "%s:%s:%s" % (hours, minutes, seconds)

print(time_of_day, 'on', num_days, 'days since epoch')
'''
Exercise 5.2. Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
 a**n + b**n = c**n
1. Write a function named check_fermat that takes four parameters—a, b, c and n—and
for any values of n greater than 2.
checks to see if Fermat’s theorem holds. If n is greater than 2 and
a**n + b**n = c**n
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”
2. Write a function that prompts the user to input values for a, b, c and n, converts them to
integers, and uses check_fermat to check whether they violate Fermat’s theorem.
'''
def check_fermat(a, b, c, n):
	if n > 2 and ((a**n + b**n)**(1/n)) == c**n:
		print('Holy smokes, Fermat was wrong!')

	else:
		print('No, that doesnt work')


def check_numbers():
	a = int(input('Chose a number for a: '))
	b = int(input('Chose a number for b: '))
	c = int(input('Chose a number for c: '))
	n = int(input('Chose a number for n: '))
	return check_fermat(a, b, c, n)

check_numbers()

'''
Exercise 5.3. If you are given three sticks, you may or may not be able to arrange them in a triangle. 
For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not be able 
to get the short sticks to meet in the middle. For any three lengths, there is a simple test to see if it is 
possible to form a triangle:

If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. 
Otherwise, you can. (If the sum of two lengths equals the third, they form what is called a 
	“degenerate” triangle.)

1. Write a function named is_triangle that takes three integers as arguments, and that prints either 
“Yes” or “No”, depending on whether you can or cannot form a triangle from sticks with the given lengths.
2. Write a function that prompts the user to input three stick lengths, converts them to integers, 
and uses is_triangle to check whether sticks with the given lengths can form a triangle.
'''

def is_triangle():
	a = int(input('Choose number for a: '))
	b = int(input('Choose number for b: '))
	c = int(input('Choose number for c: '))

	if a > b + c or b > a + c or c > a + b:
		print('Not possible')
	else:
		print('Triangle is possible')

is_triangle()










