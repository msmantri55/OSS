# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#
# Number of times bob occurs is: 2

numBobs = 0
startpoint = 0

for letter in s:
    # make startpoint nonzero
    startpoint = s.find('bob', startpoint) + 1

    # increment numBobs if search is not beginning from index 0
    if startpoint > 0:
        numBobs += 1
    else:
        # break loop if search is starting at index 0 again
        break
    
print numBobs
