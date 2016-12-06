eng2sp = dict()
eng2sp
print(eng2sp)
eng2sp['one'] = 'uno'
print(eng2sp)
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])
print(len(eng2sp))
print('one' in eng2sp)

vals = eng2sp.values()
print('uno' in vals)

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

h = histogram('brontosaurus')
print(h)

h = histogram('a')
print(h)

print(h.get('a',0))
print(h.get('a'))
print(h.get('b',0))

#11.2 Diction as collection of counters

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

h = histogram('brontosaurus')
print(h)

#11.3 Looping and dictionaries

def print_hist(h):
	for key in sorted(h):
		print(key, h[key])

h = histogram('parrot')
print(print_hist(h))

def reverse_lookup(d, v):
	for k in d:
		if d[k] == v:
			return
	raise LookupError()

h = histogram('parrot')
key = reverse_lookup(h, 2)
print(key)

def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse

known = {0:0, 1:1}

def fibonacci(n):
	if n in known:
		return known[n]
	res = fibonacci(n-1) + fibonacci(n-2)
	known[n] = res
	return res

verbose = True
def example():
	if verbose:
		print('Running example1')

been_called = False

def example2():
	been_called = True




