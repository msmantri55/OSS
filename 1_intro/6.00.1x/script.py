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