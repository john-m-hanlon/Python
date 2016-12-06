word = open('words.txt','r')
#print(word)
wordList = word.readlines()
#print(wordList[:10])
len(wordList)
#print(len(wordList))
#print(wordList[:10])
wordClean = [word.strip().lower() for word in wordList]
#print(wordClean[:10])
wordUnique = list(set(wordClean))
#print(wordUnique)
wordUnique.sort()
print(wordUnique[:10])

wordCleanTwo = sorted(list(set([word.strip().lower() for word in open('words','r')])))
print(wordCleanTwo[:10])

print('arrron\n'.strip().lower())


print(sorted('lives'))


print(sorted('lives'))
print(sorted('lives') == sorted('elvis'))
print(sorted('hated') == sorted('love'))
def signature(word):
	return ''.join(sorted(word))

print(signature('lives'))

print('/'.join(['a','b','c']))

def anagram(myword):
	return [word for word in wordClean if signature(word) == signature(myword)]

print(anagram('dictionary'))


import collections


words_bySig = collections.defaultdict(list)

for word in wordClean:
	words_bySig[signature(word)].append(word)

#print(words_bySig)

def anagram_fast(myword):
	return words_bySig[signature(myword)]

print(anagram_fast('dictionary'))

anagrams_all = {word: anagram_fast(word) for word in wordList if len(anagram_fast(word)) > 1}

print(len(anagrams_all))


