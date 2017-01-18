names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    print(' '.join(['Hello there,', name]))

'''
Print the list of names as a string, join is prefereable when concat more
than two strings
'''
print(', '.join(names))

import os

location_of_file = '/Users/JohnHanlon/Desktop/Python/Sentdex Tutorials/'\
                   'Intermediate Python 3 Tutorial [Sentdex]'
file_name = 'example.txt'

print('{}\{}'.format(location_of_file, file_name))

with open(os.path.join(location_of_file, file_name)) as f:
    print(f.read())

who = 'Gary'
how_many = 12

# Gary bought 12 apples today

print('{} bought {} apples today'.format(who, how_many))
