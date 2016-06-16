# Convert the following code into code that uses a for loop.

# print "Hello!"
# print 10
# print 8
# print 6
# print 4
# print 2

print 'Hello!'
for x in xrange(10,0,-1):
	if x%2 == 0:
		print x
	x -= 2