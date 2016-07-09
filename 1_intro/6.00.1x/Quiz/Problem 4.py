# Write a Python function that returns True if aString is a palindrome (reads 
# the same forwards or reversed) and False otherwise. Do not use Python's 
# built-in reverse function or aString[::-1] to reverse strings.

# This function takes in a string and returns a boolean.

def isPalindrome(aString):
    '''
    aString: a string
    '''
    for i in range(0, len(aString)):
        if not aString[i] == aString[(len(aString) - 1) - i]:
            return False
    return True