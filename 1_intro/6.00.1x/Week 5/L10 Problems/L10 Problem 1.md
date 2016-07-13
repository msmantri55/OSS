In this problem, we'll examine how indirection works. Consider the following definitions:

```
a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]
```

1. What is the value of the following expressions? If you think there will be an error, please type in 'error' (without quotes) in the input box.

    1. `a[0]`
    
        1

    1. `b[1]`
    
        0

    1. `a[a[1]]`
    
        3

    1. `b[b[2]]`
    
        2

    1. `a[b[2]]`
    
        3

    1. `c[a[b[3]]]`
    
        3

    1. `a[c[a[b[0]]]]`
    
        error

    1. `a[c[a[b[3]]]]`
    
        4

2. Assume we have defined the following function:

```
def foo(L):
    val = L[0]
    while (True):
        val = L[val]
```

Which of the following statement(s) will result in an infinite loop?

* foo(a)
* foo(b)
* foo(c)
* **foo(a) , foo(b)**

3. Consider the following code:

```
num = ???
L = [5, 0, 2, 4, 6, 3, 1]
val = 0
for i in range(0, num):
    val = L[L[val]]

print val
```

    1. What is the smallest value that num can be such that the number 3 is printed?

        * 0
        * **1**
        * 3
        * 5
        * Impossible

    Now, we redefine L to be:

    `L = [2, 0, 1, 5, 3, 4]`

    2. What is the smallest value that num can be such that the number 3 is printed?

        * 0
        * 3
        * 5
        * **Impossible**