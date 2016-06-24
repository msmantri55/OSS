Assume we've made the following assignment:

`x = (1, 2, (3, 'John', 4), 'Hi')`

`x[0]`

int

1

`x[2]`

tuple

(3, 'John', 4)

`x[-1]`

string

'Hi'

`x[2][2]`

int

4

`x[2][-1]`

int

4

`x[-1][-1]`

string

'i'

`x[-1][2]`

NoneType

error

`x[0:1]`

tuple

(1,)

`x[0:-1]`

tuple

(1, 2, (3, 'John', 4))

`len(x)`

int

4

`2 in x`

boolean

True

`3 in x`

boolean

False

`x[0] = 8`

NoneType

error

