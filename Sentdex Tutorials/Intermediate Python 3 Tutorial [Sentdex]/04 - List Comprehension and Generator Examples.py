""" This file contains code for use with "Intermediate Python Programming" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

for i in range(5):
    print(i)

# list comprehension, does store into memory (RAM)
xyz = [i for i in range(5)]
print(xyz)

xyz = []
for i in range(5):
    xyz.append(i)
print(xyz)

# now a generator with the (), does not store into memory (RAM)
xyz = (i for i in range(5)) 
print(xyz)
