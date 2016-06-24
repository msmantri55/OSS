# Consider the following sequence of expressions:

# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')

# We want to write some simple procedures that work on dictionaries to return information.

# This time, write a procedure, called biggest, which returns the key corresponding to the
# entry with the largest number of values associated with it. If there is more than one such
# entry, return any one of the matching keys.

# Example usage:

# >>> biggest(animals)
# 'd'

# If there are no values in the dictionary, biggest should return None. 

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) == 0:
        return None
    else:
        l = 0
        values = []
        for value in aDict.values():
            if len(value) > l:
                l = len(value)
                values = value
        for key in aDict.keys():
            if aDict[key] == values:
                return key

print biggest({})
print biggest({'G': []})
print biggest({'a': [5, 17, 4, 11, 13, 2, 8, 4], 'c': [11, 3, 8, 14], 'b': [16], 'd': []})
print biggest({'a': [8, 12, 5, 16, 8, 0, 7], 'b': [3, 12, 18, 11, 20, 0, 19, 16, 6, 14]})
print biggest({'a': [19, 15, 12, 3, 12, 9, 17, 5, 3]})
print biggest({'a': [6], 'b': [9, 20, 14, 4, 8, 4, 10]})
print biggest({'a': [19, 16, 9, 7]})
print biggest({'a': [2, 1, 10, 19, 6, 11, 1, 17, 11, 19], 'c': [7, 8], 'b': [11, 0, 17, 19, 10, 10, 3, 17], 'd': [9, 14, 9, 13]})
print biggest({'a': [1, 3, 12, 3, 9, 4, 7], 'c': [], 'b': [3, 2, 3, 18, 0], 'e': [3], 'd': [7, 7]}) 
print biggest({'a': [0, 1, 1, 4], 'c': [1, 11, 4, 5, 2, 19, 15], 'b': [0, 12, 5, 16, 2]})