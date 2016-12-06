fruit = 'banana'
letter = fruit[1]
i = 1
x = fruit[i+1]
print(x)
length = len(fruit)
last = fruit[length-1]
print(last)

index = 0
while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

print('backwards')
index = len(fruit) - 1

while index >= 0:
	letter = fruit[index]
	print(letter)
	index = index - 1

print('for loop')
for letter in fruit:
	print(letter)

for i in fruit:
	print(i)

print('prefixes')
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	if letter == 'O' or letter == 'Q':
		suffix2 = 'uack'
		print(letter + suffix2)
	else:
		print(letter + suffix)

s = 'Monty Python'
print(s[0:5])
print(s[6:len(s)])


fruit = 'banana'
print(fruit[:3])
print(fruit[3:])
print(fruit[3:3])
print(fruit[:])

greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

def find(word, letter, start):
	index = start
	while index < len(word):
		if word[index] == letter:
			print('found')
			return index
			index = index + 1
		else:
			print('not found')
			index = index + 1

	return -1

find('john','j',0)


word = 'bannaa'
count = 0
for letter in word:
	if letter == 'a':
		count += 1
print(count)


print('counter')
def counter(word, letter):
	count = 0
	for i in word:
		if i == letter:
			count += 1
			
		else:
			pass
	print(count)

counter('john','j')

word = 'banana'
new_word = word.upper()
print(new_word)

index = word.find('a')
print(index)

print(word.find('na'))
print(word.find('na', 3))
print(word.find('na', 1, 2))

print('a' in 'banana')
print('seed' in 'banana')

def in_both(word1, word2):
	for letter in word1:
		if letter in word2:
			print(letter)

in_both('apples', 'oranges')

if word == 'banana':
	print('All right, bannaa.')

if word < 'banana':
	print('Your word, ' + word + ', comes before bananas.')
elif word > 'banana':
	print('Your word, ' + word + ', comes after bananas.')

else:
	print('All right, bananas')


def is_reverse(word1, word2):
	if len(word1) != len(word2):
		return False

	i = 0
	j = len(word2) - 1

	while j > 0:
		if word1[i] != word2[j]:

			return False
		i += 1
		j -= 1
	print(word2,'is the reverse of,', word1)
	return True

is_reverse('john','nhoj')
