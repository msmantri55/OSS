# Consider the following sequence of expressions:

# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')

# We want to write some simple procedures that work on dictionaries to return
# information.

# First, write a procedure, called howMany, which returns the sum of the number
# of values associated with a dictionary. For example:

# >>> print howMany(animals)
# 6

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    total = 0
    for value in aDict.values():
        total += len(value)
    return total

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print howMany(animals)