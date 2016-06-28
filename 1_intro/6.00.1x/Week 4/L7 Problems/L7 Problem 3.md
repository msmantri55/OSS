Consider the following function definition:

```
def maxOfThree(a,b,c) :
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c        
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger
```

Assume that maxOfThree is called with numbers as arguments.

Which of the following test suites would make a path-complete glass box test suite for maxOfThree?

**Test Suite A: `maxOfThree(2, -10, 100)`, `maxOfThree(7, 9, 10)`, `maxOfThree(6, 1, 5)`, `maxOfThree(0, 40, 20)`**

Test Suite B: `maxOfThree(10, 100, -20)`, `maxOfThree(99, 0, 20)`, `maxOfThree(1, 60, 300)`

Test Suite C: `maxOfThree(0, 0, 0)`, `maxOfThree(-3, -10, -1)`, `maxOfThree(10, 30, 100)`, `maxOfThree(0, -9, 11)`, `maxOfThree(-10, 0, 30)`