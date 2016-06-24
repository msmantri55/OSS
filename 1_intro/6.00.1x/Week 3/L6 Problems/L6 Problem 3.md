Assume we've made the following assignment:

`x = [1, 2, [3, 'John', 4], 'Hi']`

Additionally, assume that the expressions are evaluated in the order shown - that is, each problem part is evaluated directly after the previous problem part(s).

`x[0]`

int

1

`x[2]`

list

[3, 'John', 4]

`x[-1]`

string

'Hi'

`x[2][2]`

int

4

`x[0:1]`

list

[1]

`2 in x`

boolean

True

`3 in x`

boolean

False

```
x[0] = 8
x
```

list

[8, 2, [3, 'John', 4], 'Hi']