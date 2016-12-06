def countdown(n):
	while n > 0:
		print(n)
		n = n - 1
		pass
	print('Blast off!')

countdown(5)

def sequence(n):
	while n != 1:
		print(n)
		if n % 2 == 0:
			n = n / 2 #n is even
		else:
			n = n*3 + 1 #n is odd
		pass
	print(n)

sequence(2)

def input_loop():
	while True:
		line = input('> ')
		if line == 'done':
			break
		print(line)

	print('Done!')

a = 4
x = 3
y = (x + a/x) / 2
print(y)
x = y
y = (x + a/x) / 2
print(y)
x = y
y = (x + a/x) / 2
print(y)

while True:
	print(x)
	epsilon = 0.00000000001
	y = (x + a/x) / 2
	if abs(y-x) < epsilon:
		print(epsilon)
		break
	x = y
	pass


import math

def newtons(n):
	n = float(n)
	x = n / 2
	i = 0
	while i < 10:
		y = (x + n/x) / 2
		x = y
		i += 1
	return y


def libmath(n):
	n = float(n)
	return math.sqrt(n)

def printout():
	print('{:<12}\t{:<12}\t{}'.format('newtons', 'libmath', 'delta'))
	for i in range(1, 10):
		n = newtons(i)
		l = libmath(i)
		ab = abs(n - 1)
		print('{:<12}\t{:<12}\t{}'.format(n, l, ab))

printout()


def input_loop():
	while True:
		n = input('> ')
		if n == 'done':
			break
		else:
			result = eval(n)
			print(result)
	print(result)


#input_loop()

#from __future__ import print function, division
#import math

def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result

def estimate_pi():
	total = 0
	k = 0
	factor = 2 * math.sqrt(2) / 9801
	while True:
		num = factorial(4*k) * (1103 + 26930*k)
		den = factorial(k)**4 * 396**(4*k)
		term = factor * num / den
		total += term

		if abs(term) < 1*10**-15:
			break
		k +=1
	return 1 / total

print('Print Srini')
print(estimate_pi())



