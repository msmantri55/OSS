Enter the value of the expressions below. 

```
def foo(x):
   def bar(x):
      return x + 1
   return bar(x * 2)
foo(3)
```

7

```
def foo (x):
   def bar (z):
      return z + x
   return bar(3)

foo(2)
```

5

