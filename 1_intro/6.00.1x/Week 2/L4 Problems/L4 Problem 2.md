```
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
```

`a(False, 2, 3)`

int

3

`b(3, 2)`

int

3

`a(3>2, a, b)`

function

function

`b(a, b)`

function

function

Perhaps contrary to expectations, in Python it is legal to compare functions! 