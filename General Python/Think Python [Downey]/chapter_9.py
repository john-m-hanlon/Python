#fin = open('words.txt')
#print(fin.readline())
#line = fin.readline()
#word = line.strip()
#print(word)

'''
fin = open('words.txt')
#for line in fin:
#	word = line.strip()
#	print(word)
for line in fin:
	word = line.strip()
	if len(word) > 20:
		print(word)
'''

print('Exercise 9.2')


fin = open('words.txt')
line = fin.readline()
word = line.strip()

def has_no_e(word):
	for i in word:
		if i == 'e':
			return False
	return True

def count_total(word):
	for i in word:
		if len(i) > 0:
			return True
	return False



count = 0
for line in fin:
	word = line.strip()
	if has_no_e(word):
		count += 1
print(count)



#percent = count / count2
#print(percent)


