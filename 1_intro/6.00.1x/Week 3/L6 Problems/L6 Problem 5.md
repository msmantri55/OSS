```
>>> aList = range(1, 6)
>>> bList = aList
>>> aList[2] = 'hello'
>>> aList == bList
```

boolean

True

`>>> aList is bList`

boolean

True

`>>> aList`

list

[1, 2, 'hello', 4, 5]

`>>> bList`

list

[1, 2, 'hello', 4, 5]

```
>>> cList = range(6, 1, -1)
>>> dList = []
>>> for num in cList:
        dList.append(num)
>>> cList == dList
```

boolean

True

`>>> cList is dList`

boolean

False

```
>>> cList[2] = 20
>>> cList
```

list

[6, 5, 20, 3, 2]

`>>> dList`

list

[6, 5, 4, 3, 2]