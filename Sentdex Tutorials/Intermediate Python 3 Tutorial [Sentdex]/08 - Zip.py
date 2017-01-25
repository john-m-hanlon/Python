""" This file contains code for use with "Intermediate Python Programming" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', 'b', 'c', 'd']

for a, b, c in zip(x, y, z):
    print(a, b, c)

# prints a zip object, but you can iterate ove a zip object
print(zip(x, y, z))

for i in zip(x, y, z):
    print(i)

print(list(zip(x, y, z)))

# with two values, can convert zip to a dict
print(dict(zip(x, y)))

[print(a, b, c) for a, b, c in zip(x, y ,z)]

[print(x, y) for x, y in zip(x, y)]
print(x)

for x, y in zip(x, y):
    print(x, y)
