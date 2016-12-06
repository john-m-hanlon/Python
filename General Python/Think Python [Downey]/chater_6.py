import math

def area(radius):
	a = math.pi * radius**2
	print('The area is: ',a)
	return a

area(5)

def absolute_value(x):
	if x < 0:
		return -x
	elif x < 0:
		return x
	else:
		return x

print(absolute_value(0))

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	print('dx is', dx)
	print('dy is', dy)
	dsquared = dx**2 + dy**2
	print('dsquared is:', dsquared)
	result = math.sqrt(dsquared)
	print('The distance is: ',result)
	return result


def hypotenuse():
	print('Run hypotenuse calculator...')
	a = int(input('Choose number for a: '))
	b = int(input('Choose number for b: '))

	sidesSquared = a**2 + b**2
	c = math.sqrt(sidesSquared)
	print('The hypotenuse is: ',c)
	return c

def circle_area(xc, yc, xp, yp):
	radius = distance(xc, yc, xp, yp)
	result = area(radius)
	return result

def is_divisible(x, y):
	if x % y == 0:
		print(True)
		return True
	else:
		print(False)
		return False

is_divisible(4,2)

def is_between(x, y, z):
	if x <= y <= z:
		print(True)
		return True
	else:
		print(False)
		return False

is_between(5,6,7)


def factorial(n):
	if not isinstance(n, int):
		print('factorial is only defined for integers')
		return None

	elif n < 0:
		print('factorial is not defined for negative integers.')
		return None

	elif n == 0:
		return 1

	else:
		return n * factorial(n-1)
factorial(0)

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return (fibonacci(n-1) + fibonacci(n-2))


def factorialv2(n):
	space = ' ' * (4 * n)
	print(space, 'factorial', n)
	if n == 0:
		print(space, 'returning 1')
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		print(space, 'returning', result)
		return result


factorialv2(3)


def is_power():
	a = int(input('This is the input for a: '))
	b = int(input('This is the input for b: '))

	if a%b == 0:
		print('True')
		return True
	else:
		print('False')
		return False


def gcd(a, b):
	while b:
		r = a%b
		a, b = b, r
	return a

print(gcd(20,8))

