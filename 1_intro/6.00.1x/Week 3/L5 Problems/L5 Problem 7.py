# For this problem, write a recursive function, `lenRecur`, which computes the
# length of an input argument (a string), by counting up the number of
# characters in the string.

def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''

    n = 0

    if aStr == '':
        return 0
    else:
        n += 1
        return n + lenRecur(aStr[1:])