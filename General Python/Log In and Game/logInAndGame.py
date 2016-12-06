from random import *

correct = True
while correct:
	name = input('What is the user name?: ').lower()
	if name == 'john':
		pw = input('Please enter your password: ')
		if pw == 'test':
			print('You may progress to the guessing game.')
		

			play = True
			while play:
				highNumb = randint(40,100)
				lowNumb = randint(1,highNumb - 15)
				answer = randint(lowNumb + 1, highNumb - 1)

				guesses = 0
				print('Guess that number between ', lowNumb, 'and ', highNumb)
				guess = int(input('Please enter your guess: '))

				while guess != answer:
					if guess > answer and guess > highNumb:
						print('Value out of range. Please try retry your guess.')
						guesses += 1
						print('Guess number: ', guesses)
						guess = int(input('Please enter your guess: '))

					if guess < answer and guess < lowNumb:
						print('Value out of range. Please try retry your guess.')
						guesses += 1
						print('Guess number: ', guesses)
						guess = int(input('Please enter your guess: '))

					if guess > answer:
						print('Guess too high, please try again.')
						guesses += 1
						print('Guess number: ', guesses)
						guess = int(input('Please enter your guess: '))

					if guess < answer:
						print('Guess too low, please try again.')
						guesses += 1
						print('Guess number: ', guesses)
						guess = int(input('Please enter your guess: '))

					if guess == answer:
						print('Correct! The answer was ', answer, 'and you guessed the number in ', guesses, 'attempts.')

						retry = input('Thank you for playing, would you like to play again? (Y/N)?: ')
						if retry == 'Y'.lower():
							play = True
						else:
							print('Thank you for playing the game.')
							print('Goodbye.')
							quit()

		if pw != 'test':
			pwi = input('Password incorrect, would you try to try the username and password again? (Y/N): ')
			if pwi == 'y'.lower():
				correct = True

			else:
				print('Thank you for trying to login, goodbye.')

	if name != 'john'.lower():
		uni = input('Username incorrect, would you like to try the username again? (Y/N): ')
		if uni == 'Y'.lower():
			correct = True
		else:
			print('Thank you for trying to login, goodbye.')