# Convert the following code into code that uses a for loop.

# print 2
# print 4
# print 6
# print 8
# print 10
# print "Goodbye!"

for x in xrange(1,11):
	if x%2 == 0:
		print x
	x += 1
print 'Goodbye!'