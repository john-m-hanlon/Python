""" This file contains code for use with "Intermediate Python Programming" by
Sentdex, available from https://www.youtube.com/user/sentdex/

Transcribed by: John Hanlon
Twitter: @hanlon_johnm
LinkedIn: http://bit.ly/2fcxlEw
Github: bit.ly/2fSDp4J
"""

example = ['left', 'right', 'up', 'down']

# wrong methodology
for i in range(len(example)):
    print(i, example[i])

# Cleaner, more sense, gets rid of range(len())
for i, j in enumerate(example):
    print(i, j)

new_dict = dict(enumerate(example))
print(new_dict)

[print(i, j) for i, j in enumerate(new_dict)]