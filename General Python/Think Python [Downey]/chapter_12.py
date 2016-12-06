#Tuples are immutable

t = 'a', 'b', 'c', 'd', 'e'
t = ('a', 'b', 'c', 'd', 'e')
t1 = 'a',
print(type(t1))
t2 = ('a')
print(type(t2))
t = tuple()
print(t)

t = tuple('lupins')
print(t)

t = ('a', 'b', 'c', 'd', 'e')
print(t[0])
print(t[1:3])
t = ('A',) + t[1:]
print(t)

print((0, 1, 2) < (0, 3, 4))
print((0, 1, 20000) < (0, 3, 4))

addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname)
print(domain)

#12.3 Tuples as return values

t = divmod(7, 3)
print(t)

quot, rem = divmod(7, 3)
print(quot)
print(rem)
print(quot, rem)

def min_max(t):
	return min(t), max(t)

print(min_max(t))

def printall(*args):
	print(args)

printall(1, 2.0, '3')

s = 'abc'
t = [0, 1, 2]

print(zip(s, t))

for pair in zip(s, t):
	print(pair)

print(list(zip(s, t)))

print(list(zip('Anne', 'Elk')))

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
	print(number, letter)

def has_match(t1, t2):
	for x, y in zip(t1, t2):
		if x == y:
			return True
	return False

for index, element in enumerate('abc'):
	print(index, element)

#12.6 Dictionaries and tuples
d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)

for key, value in d.items():
	print(key, value)


t = [('a', 0), ('b', 1), ('c', 2)]
d = dict(t)
print(d)

d = dict(zip('abc', range(3)))
print(d)

`