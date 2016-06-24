def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

'''
  >>> print testList
  [1, 4, 8, 9]
'''

applyToEach(testList, abs)

'''
  >>> print testList
  [2, -3, 9, -8]
'''

def plusOne(a):
    return a + 1

applyToEach(testList, plusOne)

'''
  >>> print testList
  [1, 16, 64, 81]
'''

def square(a):
    return a**2

applyToEach(testList, square)