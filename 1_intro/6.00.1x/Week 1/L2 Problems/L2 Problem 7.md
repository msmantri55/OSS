For each of the expressions below, specify its type and value. If it generates an error, select type 'NoneType' and write the word 'error' (note this is a word, not a string) in the box for the value. While you could simply type these expressions into an Idle shell, we encourage you to answer them directly since this will help reinforce your understand of basic Python expressions.

Assume we've made the following assignments:

```
> str1 = 'hello'
> str2 = ','
> str3 = 'world'
```

Note: The Python 'in' operator

1) `str1`
string

hello

2) `str1[0]`

string

h

3) `str1[1]`

string

e

4) `str1[-1]`
string

o

5) `len(str1)`
int

5

6) `str1[len(str1)]`
NoneType

error

7) `str1 + str2 + str3`

string

hello,world

8) `str1 + str2 + ' ' + str3`

string

hello, world

9) `str3 * 3`

string

worldworldworld

10) `'hello' == str1`

boolean

True

11) `'HELLO' == str1`

boolean

False

12) `'a' in str3`

boolean

False

13)
```
str4 = str1 + str3
'low' in str4
```

boolean

True

14) `str3[1:3]`

string

or

15) `str3[:3]`

string

wor

16) `str3[:-1]`

string

worl

17) `str1[1:]`

string

ello

18) `str4[1:9]`

string

elloworl

19) `str4[1:9:2]`

string

elwr

20) `str4[::-1]`

string

dlrowolleh