a = [10, 20, 30, 40]
b = ['crunch frog', 'ram bladder', 'lark vomit']
c = ['spam', 2.0, 5, [10, 20]]
cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123]
empty = []
print(cheeses, numbers, empty)

numbers[1] = 5
print(numbers)

cheeses = ['Cheedar', 'Edam', 'Gouda']

print('Edam' in cheeses)

for cheese in cheeses:
	print(cheese)

print(numbers)
#print(range(numbers))
print(len(numbers))

for i in range(len(numbers)):
	numbers[i] = numbers[i] * 2
	print(numbers)


for x in []:
	print('This never happens')


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

print([0] * 4)
print(a * 3)

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
t[1:3] = ['x', 'y']
print(t)

t = ['a', 'b', 'c']
t.append('d')
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)

def add_all(t):
	total = 0
	for x in t:
		total += x
	return total

t = [1, 2, 3]
print(sum(t))

def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res

def only_upper(t):
	res = []
	for s in t:
		if s.isupper():
			res.append(s)
		return res

t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)

t = ['a', 'b', 'c']
del t[1]
print(t)

t = ['a', 'b', 'c']
t.remove('c')
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)

s = 'spam'
t = list(s)
print(t)

s = 'pining for the fjords'
t = s.split()
print(t)

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
print(t)

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
s = delimiter.join(t)
print(s)

a = 'banana'
b = 'banana'

print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

a = [1, 2, 3]
b = a
print(b is a)

b[0] = 42
print(a)

def delete_head(t):
	del t[0]

letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)

t3 = t1 + [4]
print(t1)
print(t3)

def bad_delete_head(t):
	t = t[1:]

t4 = [1, 2, 3]
bad_delete_head(t4)
print(t4)

def tail(t):
	return t[1:]

letters = ['a', 'b', 'c']
rest = tail(letters)
print(rest)




