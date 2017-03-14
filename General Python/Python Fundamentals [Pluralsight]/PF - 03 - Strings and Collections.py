#
# A simple program to count the words in a given text
# PF - 03 - Strings and Collections.py
#

__author__ = 'JohnHanlon'

x = 'sdf''sdf'

print(x)

x = 'hello \nhow are you'
print(x)

x = 'a backslash \\ is here'
print(x)

c = 'oslo'
print(c.capitalize())


def chap_3_example():
    ''' Function that reads through a story from online

    Parameters
    ==========
    N/A : takes no parameters

    Returns
    =======
    N/A : returns nothing
    '''

    from urllib.request import urlopen
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        print(story_words)


print(chap_3_example())
