import math
class Point:
	'''Represents a point in 2-D space'''

print(Point)

blank = Point()
print(blank)

blank.x = 3.0
blank.y = 4.0

print(blank.y)

x = blank.x

print(x)
print('(%g, %g)' % (blank.x, blank.y))
distance = math.sqrt(blank.x**2 + blank.y**2)
print(distance)

def print_point(p):
	print('(%g, %g)' % (p.x, p.y))

print(print_point(blank))

def distance_between_points(a,b):
	print(int(a - b))

distance_between_points(4,5)

class Rectange:
	'''Represents a rectangle. 

	attributes: width, height, corners.
	'''
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
	p = Point()
	p.x = rect.corner.x + rect.width/2
	p.y = rect.corner.y + rect.height/2
	return p

