Consider the following function definition:

```
def foo(x, a):
   """
   x: a positive integer argument
   a: a positive integer argument

   returns an integer
   """
   count = 0
   while x >= a:
      count += 1
      x = x - a
   return count
```

Please select the best glass box test suite for the function foo from the following options.

Test Suite A: `foo(2, 5)`, `foo(5, 6)`, `foo(9, 7)`
Test Suite B: `foo(10, 3)`, `foo(1, 4)`, `foo(10, 6)`
Test Suite C: `foo(100, 5)`, `foo(96, 5)`, `foo(22, 5)`