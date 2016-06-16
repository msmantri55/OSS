As we'll see in subsequent lectures, everything in Python is an object. Objects are special because we can associate special functions, referred to as object methods, with the object. In this problem you'll be working with string objects, and their built-in methods.

A complete description of the methods available to string objects can be found in the [Python library reference on string methods](http://docs.python.org/library/stdtypes.html#string-methods). Another useful resource about string methods [can be found here](http://www.greenteapress.com/thinkpython/html/thinkpython009.html#toc93).

In this exercise, we want you to get some experience in using methods as functions. The convention for object methods is to use the "dot" notation, so that if s is a string, evaluating s.upper will return the actual function, and evaluating s.upper() will cause the function itself to be evaluated (in this case it returns a new string, since strings are immutable) with every character now in upper case. An example of this follows:

```
>>> s = 'abc'
>>> s.capitalize
<built-in method capitalize of str object at 0x104c35878>
>>> s.capitalize()
'Abc'
```

For each of the expressions in this problem, specify its type and value. If it generates an error, select type 'NoneType' and put the word 'error' in the box for the value. If it would be a function, select type 'function' and put the word 'function' in the box for the value.

Assume we've made the following assignments:

```
> str1 = 'exterminate!'
> str2 = 'number one - the larch'
```

Assume that the expressions are evaluated in the order shown - that is, each problem part is evaluated directly after the previous problem part(s).

`str1.upper`

function

function

`str1.upper()`

string

EXTERMINATE!

`str1`

string

exterminate!

`str1.isupper()`

boolean

False

`str1.islower()`

boolean

True

str2 = str2.capitalize()
`str2`

string

Number one - the larch

`str2.swapcase()`

string

nUMBER ONE - THE LARCH

`str1.index('e')`

int

0

`str2.index('n')`

int

8

`str2.find('n')`

int

8

`str2.index('!')`

NoneType

error

`str2.find('!')`

int

-1

Note: Be sure to make note of the difference between the find and index string methods...

`str1.count('e')`

int

3

str1 = str1.replace('e', '*')
`str1`

string

*xt*rminat*!

`str2.replace('one', 'seven')`

string

Number seven - the larch

