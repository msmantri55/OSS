```
myStr = '6.00x'

for char in myStr:
    print char

print 'done' 
```

1. How many times does 6 print out?
1

2. How many times does . print out?
1

3. How many times does 0 print out?
2

4. How many times does x print out?
1

5. How many times does done print out? 
1

```
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print letter 
    print letter

print 'done'
```

1. How many times does H print out?
1

2. How many times does e print out? Disregard the letters in the word done.
2

3. How many times does l print out?
3

4. How many times does o print out? Disregard the letters in the word done.
1

5. How many times does ! print out?
2

6. How many times does done print out? 
1

```
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons) 
```

1. How many times does o print out? Disregard the o's in last two print statements.
0

2. How many times does M print out?
1

3. What will the value of the variable numVowels be?
11

4. What will the value of the variable numCons be? 
-25