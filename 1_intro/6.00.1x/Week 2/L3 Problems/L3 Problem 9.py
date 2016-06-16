# In this problem, you'll create a program that guesses a secret number!

# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

print 'Please think of a number between 0 and 100!'
upper = 100
lower = 0
correct = False

while not correct:
	midpoint = (upper + lower) / 2
	print 'Is your secret number ' + str(midpoint) + '?'
	response = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')

	if response == 'h':
		upper = midpoint
	elif response == 'l':
		lower = midpoint
	elif response == 'c':
		correct = True
	else:
		print 'Sorry, I did not understand your input'

print 'Game over. Your secret number was: ' + str(midpoint)