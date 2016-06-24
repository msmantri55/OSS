Suppose we evaluate the following expressions:

```
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
```

We are now going to evaluate a set of expressions, resulting in the following sequence of interactions. Fill in each blank to show what the Python interpreter would print at that point. If an expression below would generate an error, enter 'error'.

`>>> animals`

{'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd':'donkey'}

`>>> animals['c']`

'coati'

`>>> animals['donkey']`

error

`>>> len(animals)`

4

```
>>> animals['a'] = 'anteater'
>>> animals['a']
```

'anteater'

`>>> len(animals['a'])`

8

`>>> animals.has_key('baboon')`

False

`>>> 'donkey' in animals.values()`

True

`>>> animals.has_key('b')`

True

`>>> animals.keys()`
 

['a', 'b', 'c', 'd']

```
>>> del animals['b']
>>> len(animals)
```

3

`>>> animals.values()`

['anteater', 'coati', 'donkey']