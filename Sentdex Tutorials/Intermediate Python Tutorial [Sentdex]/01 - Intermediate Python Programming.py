import this

names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    print('Hello there, ' + name)
    print(' '.join(['Hello there,',name]))

print(', '.join(names))

import os

location_of_files = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/Intermediate Python Tutorial [Sentdex]/'
file_name = 'example.txt'


# with open(os.path.join(location_of_files, file_name)) as f:
#     print(f.read())

who = 'Gary'
how_many = 12

# Gary bought 12 apples today

sentence = '{} bought {} apples today'.format(who, how_many)

print(sentence)