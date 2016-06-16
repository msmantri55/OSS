Consider the following code:

```
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)
```

If this code is executed, it will print succeeded: 5.0

Now suppose we try the following:

```
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)
```

Select the answer that best describes what occurs when the above code is executed:

Script enters an infinite loop and never terminates <span> <text>Script enters an infinite loop and never terminates </text> </span> - correct

Now suppose we try

```
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)
```

Select the answer that best describes what occurs when the above code is executed:

Script successfully completes, and prints out succeeded: 5.0 <span> <text>Script successfully completes, and prints out <code>succeeded: 5.0</code> </text> </span> - correct

Finally, let's use the same code as immediately above, but change the first line to x = 23. Note that the square root of 23 is roughly 4.7958.

Select the answer that best describes what occurs when the modified code is executed:

Script successfully completes, and prints out succeeded: 5.0
Script successfully completes, but prints out failed <span> <text>Script successfully completes, but prints out <code>failed</code> </text> </span> - correct
Script successfully completes, but prints out succeeded: followed by some number not equal to 5.0
Script enters an infinite loop and never terminates

Hint: If any of the above answers confuse you, try running the code on your own machine and inserting print statements to print out intermediate values of variables so you can examine what happens to certain variables - for example, guess - as the program is executed.
