Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated. If evaluating an expression would cause an error, select NoneType and write error in the box. If the result is a function, select function and write function in the box. As always, try to do this problem by hand before turning to your interpreter for help.

Assume the following definitions have been made:

```
class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8
```

```
w1 = Weird(X, Y)
print w1.getX()
```

NoneType

error

```
print w1.getY()
```

NoneType

error

```
w2 = Wild(X, Y)
print w2.getX()
```

int

7

```
print w2.getY()
```

int

8

```
w3 = Wild(17, 18)
print w3.getX()
```

int

17

```
print w3.getY()
```

int

18

```
w4 = Wild(X, 18)
print w4.getX()
```

int

7

```
print w4.getY()
```

int

18

```
X = w4.getX() + w3.getX() + w2.getX()
print X
```

int

31

```
print w4.getX()
```

int

7

```
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print Y
```

int

44

```
print w2.getY()
```

int

8

```