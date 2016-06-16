**Code Sample**

```
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1
```

We wish to re-write the above code, but instead of nesting a for loop inside a while loop, we want to nest a while loop inside a for loop. Which of the following loops gives the same output as the Code Sample?

```
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print "Iteration " + str(iteration) + "; count is: " + str(count)
```

No, Test 1 does not give the same output as the Code Sample <span> <text>No, Test 1 does not give the same output as the Code Sample</text> </span> - correct

```
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print "Iteration " + str(iteration) + "; count is: " + str(count)
        break
```

No, Test 2 does not give the same output as the Code Sample <span> <text>No, Test 2 does not give the same output as the Code Sample</text> </span> - correct

```
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
```

Yes, Test 3 gives the same output as the Code Sample <span> <text>Yes, Test 3 gives the same output as the Code Sample</text> </span> - correct

```
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print "Iteration " + str(iteration) + "; count is: " + str(count)
```

Yes, Test 4 gives the same output as the Code Sample <span> <text>Yes, Test 4 gives the same output as the Code Sample</text> </span> - correct

```
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print "Iteration " + str(iteration) + "; count is: " + str(count)
```

Yes, Test 5 gives the same output as the Code Sample <span> <text>Yes, Test 5 gives the same output as the Code Sample</text> </span> - correct