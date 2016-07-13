For the following programs, fill in the best-case and the worst-case number of steps it will take to run each program.

For these questions, you'll be asked to write a mathematical expression. Use +, -, / signs to indicate addition, subtraction, and division. Explicitly indicate multiplication with a * (ie say "6*n" rather than "6n"). Indicate exponentiation with a caret (^) (ie "n^4" for `n`<sup>4</sup>). Indicate base-2 logarithms with the word log2 followed by parenthesis (ie "log2(n)").

1. Program 1:

```
    def program1(x):
        total = 0
        for i in range(1000):
            total += i

        while x > 0:
            x -= 1
            total += x

        return total
```

What is the number of steps it will take to run Program 1 in the best case? Express your answer in terms of n, the size of the input x.

`3003`

What is the number of steps it will take to run Program 1 in the worst case? Express your answer in terms of n, the size of the input x.

`5*n + 3003`

2. Program 2:

```
def program2(x):
    total = 0
    for i in range(1000):
        total = i

    while x > 0:
        x /= 2
        total += x

    return total
```

What is the number of steps it will take to run Program 2 in the best case? Express your answer in terms of n, the size of the input x.

`2003`

What is the number of steps it will take to run Program 2 in the worst case? Express your answer in terms of n, the size of the input x.

`5*log2(n) + 2008`

3. Program 3:

```
def program3(L):
    totalSum = 0
    highestFound = None
    for x in L:
        totalSum += x

    for x in L:
        if highestFound == None:
            highestFound = x
        elif x > highestFound:
            highestFound = x

    return (totalSum, highestFound)
```

What is the number of steps it will take to run Program 3 in the best case? Express your answer in terms of n, the number of elements in the list L.

`3`

What is the number of steps it will take to run Program 3 in the worst case? Express your answer in terms of n, the number of elements in the list L.

`7*n + 2`