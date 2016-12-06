import collections

wordClean = sorted(list(set([word.strip().lower() for word in open('words.txt','r')])))

def signature(word):
  return ''.join(sorted(word))

words_bySig = collections.defaultdict(list)

for word in wordClean:
  words_bySig[signature(word)].append(word)

def anagram_fast(myword):
  return words_bySig[signature(myword)]

anagrams_all = {word: anagram_fast(word) for word in wordClean if len(anagram_fast(word)) > 1}

words_byLength = collections.defaultdict(list)

for word in wordClean:
  words_byLength[len(word)].append(word)

#print(words_byLength)

anagrams_byLength = {}

for length, words in words_byLength.items():
  anagrams_byLength[length] = sum(len(anagram_fast(word)) - 1 for word in words if len(anagram_fast(word)) > 1)/2

print(anagrams_byLength)

print(anagrams_byLength[22])