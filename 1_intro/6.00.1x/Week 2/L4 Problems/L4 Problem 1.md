For each of the following functions, specify the type of its output. You can assume each function is called with an appropriate argument, as specified by its docstring.

```
def a(x):
   '''
   x: int or float.
   '''
   return x + 1
```

Indicate the type of the output that the function a will yield. 

num

```
def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
```

Indicate the type of the output that the function b will yield.

float

```
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y
```

Indicate the type of the output that the function c will yield.

num

```
def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y
```

Indicate the type of the output that the function d will yield.

bool

```
def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z
```

Indicate the type of the output that the function e will yield.

bool

```
def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2
```

Indicate the type of the output that the function f will yield.

NoneType

Below is a transcript of a session with the Python shell. Assume the functions from Part 1 (above) have been defined. Provide the type and value of the expressions being evaluated. If evaluating an expression would cause an error, select NoneType and write 'error' in the box. If the value of an expression is a function, select function as the type and write 'function' in the box.

`a(6)`

int

7

`a(-5.3)`

float

-4.3

`a(a(a(6)))`

int

9

`c(a(1), b(1))`

float

4.0

`d('apple', 11.1)`

boolean

True

`e(a(3), b(4), c(3, 4))`

boolean

False

`f`

function

function

