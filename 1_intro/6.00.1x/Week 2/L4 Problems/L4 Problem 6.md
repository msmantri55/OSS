Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated. If evaluating an expression would cause an error, select NoneType and write 'error' in the box. If the result is a function, select function and write 'function' in the box.

```
>>> a = 10
>>> def f(x):
      return x + a
>>> a = 3
>>> f(1)
```

int

4

```
>>> x = 12
>>> def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
>>> g(x)
```

int

19

