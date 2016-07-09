# for test purposes
def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    Lcopy = L[:]

    for element in Lcopy:
        if not f(element):
            L.remove(element)

    return len(L)

run_satisfiesF(L, satisfiesF)

# for test purposes
L = ['a', 'b', 'a']
print satisfiesF(L)
print L