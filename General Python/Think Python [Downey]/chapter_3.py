import math

degrees = 180
x = math.sin(degrees / 360.0 * 2 * math.pi)
print(x)

x1 = math.exp(math.log(x+1))
print(x1)

def print_lyrics():
	print("I'm a lumberjack, and I'm Okay.")
	print("I sleep all night and I work all day.")

print_lyrics()

def repeat_lyrics():
	x = 0
	while x < 10:
		print_lyrics()
		print_lyrics()
		x = x + 1
		print(x)

		

repeat_lyrics()

x = 'john john john'

def print_twice(bruce):
	print(bruce)
	print(bruce)

print_twice(x)

#Exercise 3.1. Write a function named right_justify that takes a string named s as a parameter and prints the 
#string with enough leading spaces so that the last letter of the string is in column 70 of the display.
#>>> right_justify('monty')
#monty
#Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len that 
#returns the length of a string, so the value of len('monty') is 5.

print('____________')
print('Exercise 3.1')
print('____________')

def right_justify(input):
	length = len(input)
	if length < 71:
		print('The length of the input is:',length,'characters')
		distanceFrom70 = 70 - length
		print('This is:',distanceFrom70,'characters away from 70')
		bufferChar = ' ' * distanceFrom70
		output = bufferChar + input
		print(output)
		print(len(output))

right_justify('timbucktu')


'''
Exercise 3.2. A function object is a value you can assign to a variable or pass as an argument. For
example, do_twice is a function that takes a function object as an argument and calls it twice:
def do_twice(f):
    f()
f()
Here’s an example that uses do_twice to call a function named print_spam twice.
def print_spam():
    print('spam')
do_twice(print_spam)
1. Type this example into a script and test it.
2. Modify do_twice so that it takes two arguments, a function object and a value, 
and calls the function twice, passing the value as an argument.
3. Copy the definition of print_twice from earlier in this chapter to your script.
4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
argument.
5. Define a new function called do_four that takes a function object and a value
and calls the function four times, passing the value as a parameter. 
There should be only two statements in the body of this function, not four.
Solution: http: // thinkpython2. com/ code/ do_ four. py .
'''

print('____________')
print('Exercise 3.2')
print('____________')

def do_twice(func, arg):
	func(arg)
	func(arg)

def print_twice(arg):
	print(arg)
	print(arg)

def do_four(func, arg):
	do_twice(func, arg)
	do_twice(func, arg)

do_twice(print_twice, 'spam')
print('')

do_four(print_twice, 'spam')


'''
Exercise 3.3. Note: This exercise should be done using only the statements 
and other features we have learned so far.
1. Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence of values:
print('+', '-')
By default, print advances to the next line, but you can override that behavior and put a
space at the end, like this:
     print('+', end=' ')
     print('-')
 
28
Chapter3. Functions
 The output of these statements is '+ -'.
A print statement with no argument ends the current line and goes to the next line.
2. Write a function that draws a similar grid with four rows and four columns.
Solution: http: // thinkpython2. com/ code/ grid. py . Credit: 
This exercise is based on an exercise in 
Oualline, Practical C Programming, Third Edition, O’Reilly Media, 1997.
'''
def boxChart():

	a = '+ '
	b = '- '
	c = ' '
	d = '| '
	e = a + 4*b + a + 4*b + a
	f = d + 8*c + d + 8*c + d
	
	def middleLoop():
		count1 = 0
		while count1 < 4:
			print(f)
			count1 = count1 + 1
			
	print(e)		
	middleLoop()
	print(e)
	middleLoop()
	print(e)

boxChart()
