# Write an iterative function, `lenIter`, which computes the length of an input
# argument (a string), by counting up the number of characters in the string.

def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    counter = 0
    for character in aStr:
        counter +=1

    return counter