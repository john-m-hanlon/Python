fruit = 'banana'
letter = fruit[1]
print(fruit[0])
print(letter)

i = 1
print(fruit[i])
print(fruit[i+1])

print(len(fruit))

length = len(fruit)
last = fruit[length - 1]
print(last)

index = 0
while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

fruit2 = 'apple'
print('backwards')
index = len(fruit2)-1
while index >= 0:
	letter = fruit2[index]
	print(letter)
	index = index - 1


print('for loop')

for letter in fruit:
	print(letter)


prefixes = 'JKLMNOPQ'
suffix = 'ack'

for i in prefixes:
	if i == 'Q':
		print(i + 'u' + suffix)
	elif i == 'O':
		print(i + 'u' + suffix)
	else:
		print(i + suffix)


print('8.4 String slices')

s = 'Monty Python'
print(s[0:5])
print(s[6:15])

print(fruit[:3])
print(fruit[3:])
print(fruit[3:3])
print(fruit[:])

greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)


print('8.6 Searching')

def find(word, letter, index):
	
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1

print(find('johnj','j',1))

print('8.7 Looping and counting')

word = 'banana'
count = 0
for letter in word:
	if letter == 'a':
		count = count + 1

print(count)

print('Exercise for 8.7')
def count(word, letter):
	count = 0
	index = 0
	for letter in word:
		if word[index] == letter:
			count = count + 1
	print(count)

word = 'banana'
new_word = word.upper()
print(new_word)
index = word.find('a')
print(index)

print(word.find('na'))

print(word.find('na',3))

name = 'bob'
print(name.find('b',1,2))

print('a' in 'banana')

def in_both(word1, word2):
	for letter in word1:
		if letter in word2:
			print(letter)

in_both('apples','oranges')

if word == 'banana':
	print('All right, bananas.')


word = 'bananas'

if word < 'bananas':
	print('Your word, ' + word + ' comes before banana')

elif word > 'bananas':
	print('Your word, ' + word + ' comes after banana')

else:
	print('All right, ' + word + ' .')

print('8.11 Debugging')

def is_reverse(word1, word2):
	if len(word1) != len(word2):
		return False

	i = 0
	j = len(word2) - 1

	while j >= 0:
		print(i, j) #print here first for debugging purpose
		
		if word1[i] != word2[j]:
			return False
		i = i+1
		j = j -1
	return True

is_reverse('pots','stop')

s = 'bananas'

print(s.count('a'))


